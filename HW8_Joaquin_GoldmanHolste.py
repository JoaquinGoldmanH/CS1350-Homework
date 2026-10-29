#Exception_Lecture1: practice_3
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print(f"  Error: '{filename}' was not found.")
            return None
        except PermissionError:
            print(f"  Error: no permission to open '{filename}'.")
            return None
        else:
            content = file.read()
            return content.strip().upper()
        finally:
            if file is not None:
                file.close()
                print(f"  '{filename}' was closed.")

    # Create a sample file so the "exists.txt" test has something to read
    with open("exists.txt", "w") as f:
        f.write("hello from exists.txt\n")

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self, fail=False):
            """Acquire resource - might fail."""
            if fail:
                raise RuntimeError(f"Could not acquire {self.name}")
            self.resource = f"{self.name} connection"
            print(f"  Acquired {self.resource}")

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                print(f"  Released {self.resource}")
                self.resource = None
            else:
                print(f"  Nothing to release for {self.name}")

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError(f"{self.name} has not been acquired")
            return f"Used {self.resource} successfully"

    # Test resource management
    rm = ResourceManager("Database")

    for should_fail in [False, True]:
        print(f"\nTest (acquire fails = {should_fail}):")
        try:
            rm.acquire(fail=should_fail)
        except RuntimeError as e:
            print(f"  Error: {e}")
        else:
            print(f"  {rm.use()}")
        finally:
            rm.release()

# Run the practice
practice_3_complete_pattern()

#Exception_Lecture2: practice_2

def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Position {position}: {reason}")

    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            self.winner = winner
            if winner:
                message = f"Player {winner} already won"
            else:
                message = "The game ended in a draw"
            super().__init__(message)

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
            self.winner = None

        def make_move(self, row, col):
            if self.game_over:
                raise GameOverError(self.winner)

            if not (0 <= row < 3 and 0 <= col < 3):
                raise InvalidMoveError((row, col), "out of bounds")

            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "already taken")

            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                self.game_over = True
                self.winner = self.current_player
            elif all(cell != ' ' for r in self.board for cell in r):
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

        def check_winner(self, player):
            b = self.board
            lines = (
                [b[i] for i in range(3)] +
                [[b[r][c] for r in range(3)] for c in range(3)] +
                [[b[i][i] for i in range(3)], [b[i][2 - i] for i in range(3)]]
            )
            return any(all(cell == player for cell in line) for line in lines)

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

    # Extra test: play until X wins, then try one more move
    game2 = TicTacToe()
    for row, col in [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (2, 2)]:
        try:
            game2.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")


# Run the practice
practice_2_custom_exceptions()

#Exception_Lecture2: practice_3
import os


def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # TODO: Build a file processing system with proper error handling

    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None
            try:
                file = open(filename, "r")
                content = file.read()
            except FileNotFoundError:
                self.failed_files.append((filename, "File not found"))
                print(f"❌ {filename}: file not found")
                return None
            except PermissionError:
                self.failed_files.append((filename, "Permission denied"))
                print(f"❌ {filename}: permission denied")
                return None
            except Exception as e:
                self.failed_files.append((filename, f"{type(e).__name__}: {e}"))
                print(f"❌ {filename}: unexpected error ({type(e).__name__})")
                return None
            else:
                line_count = len(content.splitlines())
                word_count = len(content.split())
                self.processed_files.append(filename)
                print(f"✅ {filename}: {line_count} lines, {word_count} words")
                return content
            finally:
                if file is not None:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            try:
                names = sorted(os.listdir(directory))
            except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
                self.failed_files.append((directory, f"{type(e).__name__}: {e}"))
                print(f"❌ {directory}: could not open directory")
                return

            for name in names:
                path = os.path.join(directory, name)
                if os.path.isfile(path):
                    self.process_file(path)  # errors are caught inside, so the loop continues

        def get_report(self):
            """
            Get processing report.
            """
            total = len(self.processed_files) + len(self.failed_files)
            return {
                "total": total,
                "succeeded": len(self.processed_files),
                "failed": len(self.failed_files),
                "processed_files": self.processed_files,
                "failed_files": self.failed_files,
            }

    # Create a sample file so the "valid.txt" test has something to read
    with open("valid.txt", "w") as f:
        f.write("This is a valid file.\nIt has two lines.\n")

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")

    # Extra test: process a whole directory
    os.makedirs("sample_dir", exist_ok=True)
    for name in ["a.txt", "b.txt"]:
        with open(os.path.join("sample_dir", name), "w") as f:
            f.write(f"Contents of {name}\n")

    dir_processor = FileProcessor()
    dir_processor.process_directory("sample_dir")
    dir_processor.process_directory("no_such_dir")
    print(f"Directory report: {dir_processor.get_report()}")

# Run the practice
practice_3_complete_system()