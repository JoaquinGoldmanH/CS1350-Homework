# ============================================================
# Problem 1: Security Log Splitter and Status Report
# ============================================================

def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.
    Args:
        machines: dict mapping machine name -> log file name
    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}

    with open("info.log", "w") as info_out, \
         open("warning.log", "w") as warning_out, \
         open("error.log", "w") as error_out:

        outputs = {"INFO": info_out, "WARNING": warning_out, "ERROR": error_out}

        for machine, log_file in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}

            with open(log_file, "r") as log:
                for line in log:
                    line = line.strip()
                    if line == "":
                        continue

                    for level in outputs:
                        if f"[{level}]" in line:
                            outputs[level].write(f"{machine} | {line}\n")
                            counts[machine][level] += 1
                            break

    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    total_info = 0
    total_warning = 0
    total_error = 0

    for machine, levels in counts.items():
        info = levels["INFO"]
        warning = levels["WARNING"]
        error = levels["ERROR"]
        entries = info + warning + error

        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(f"{machine}: {entries} entries | INFO {info} | WARNING {warning} "
              f"| ERROR {error} | Status: {status}")

        total_info += info
        total_warning += warning
        total_error += error

    print("-" * 40)
    total = total_info + total_warning + total_error
    print(f"Total: {total} entries | INFO {total_info} | WARNING {total_warning} "
          f"| ERROR {total_error}")

    print(f"Errors (see {error_file}):")
    with open(error_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            if line:
                print(f"  {line}")


# Test cases
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)


# ============================================================
# Problem 2: Incident Tracker
# ============================================================

import json
import pickle
import os


def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []

    with open(csv_file, "r") as f:
        next(f)  # skip the header line
        for line in f:
            line = line.strip()
            if line == "":
                continue
            incident_id, machine, severity, description = line.split(",")
            incidents.append({
                "id": int(incident_id),
                "machine": machine,
                "severity": severity,
                "description": description,
            })

    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    by_machine = {}
    by_severity = {}
    high_ids = []

    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]
        by_machine[machine] = by_machine.get(machine, 0) + 1
        by_severity[severity] = by_severity.get(severity, 0) + 1
        if severity == "high":
            high_ids.append(incident["id"])

    summary = {
        "total": len(incidents),
        "by_machine": by_machine,
        "by_severity": by_severity,
        "high_ids": high_ids,
    }

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    by_machine = {}
    for incident in incidents:
        by_machine.setdefault(incident["machine"], []).append(incident)

    for machine, machine_incidents in by_machine.items():
        with open(os.path.join(folder, f"{machine}.json"), "w") as f:
            json.dump(machine_incidents, f, indent=2)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)


# Test cases
with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")
print(len(incidents))
print(incidents[0])

summary = save_summary(incidents, "summary.json")
print(summary)

with open("summary.json", "r") as f:
    print(json.load(f) == summary)

print(archive(incidents, "archive"))

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])

restored = load_archive("archive")
print(restored == incidents)


# ============================================================
# Problem 3 (Bonus): Workspace Organizer and Backup System
# ============================================================

import os
import shutil


def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""
    destinations = {
        ".log": "logs",
        ".csv": "data",
        ".json": "data",
        ".pkl": "pickles",
    }
    moved = {"logs": [], "data": [], "pickles": [], "other": []}

    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue  # leave existing subfolders alone

        extension = os.path.splitext(name)[1].lower()
        subfolder = destinations.get(extension, "other")

        target_dir = os.path.join(folder, subfolder)
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(path, os.path.join(target_dir, name))
        moved[subfolder].append(name)

    for key in moved:
        moved[key].sort()

    return moved


def create_backup(source_dir, backup_root, label):
    """Copy source_dir to backup_root/backup_<label>; return the new path."""
    os.makedirs(backup_root, exist_ok=True)
    backup_dir = os.path.join(backup_root, f"backup_{label}")
    shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)
    return backup_dir


def verify_backup(source_dir, backup_dir):
    """Return True if every file under source_dir is in backup_dir with the same size."""
    for current_dir, subdirs, files in os.walk(source_dir):
        for name in files:
            source_file = os.path.join(current_dir, name)
            relative = os.path.relpath(source_file, source_dir)
            backup_file = os.path.join(backup_dir, relative)

            if not os.path.isfile(backup_file):
                return False
            if os.path.getsize(source_file) != os.path.getsize(backup_file):
                return False

    return True


def cleanup_old_backups(backup_root, keep):
    """Delete all but the newest `keep` backups; return sorted names deleted."""
    backups = sorted(
        name for name in os.listdir(backup_root)
        if os.path.isdir(os.path.join(backup_root, name))
    )

    number_to_delete = max(len(backups) - keep, 0)
    to_delete = backups[:number_to_delete]

    for name in to_delete:
        shutil.rmtree(os.path.join(backup_root, name))

    return sorted(to_delete)


# Test cases
# Start clean so the test can be re-run
for old in ["workspace", "backups"]:
    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")
for name in ["a.log", "b.log", "incidents.csv", "summary.json", "incidents.pkl",
             "notes.txt"]:
    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))
print(sorted(os.listdir("workspace")))

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
    path = create_backup("workspace", "backups", label)
    print(os.path.basename(path), verify_backup("workspace", path))

# Damage one backup: verification must now fail
os.remove(os.path.join("backups", "backup_2026-10-03", "logs", "a.log"))
print(verify_backup("workspace", os.path.join("backups", "backup_2026-10-03")))

print(cleanup_old_backups("backups", 2))
print(sorted(os.listdir("backups")))
