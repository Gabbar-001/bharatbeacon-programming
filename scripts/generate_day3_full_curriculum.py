# Script to generate comprehensive 10-15 minute curriculum for Day 3
import sys
from pathlib import Path

BASE_DIR = Path("D:/bharatbeacon-programming")
CONTENT_DIR = BASE_DIR / "content_plan"

day3_data_code = '''# Day 3 Masterclass Data Definitions (Full 10-15 Minute Curriculum)
from src.tech_animator import COLOR_PYTHON, COLOR_JAVA, COLOR_MONGO, COLOR_SQL

DAY3_MASTERCLASSES = [
    # =========================================================================
    # 1. PYTHON DAY 3 MASTERCLASS (Target: 11 - 13 Minutes)
    # =========================================================================
    {
        "track": "python",
        "track_title": "PYTHON MASTERCLASS",
        "episode_info": "DAY 03 OF 60",
        "title": "Python Day 3: Mastering List Comprehensions, Generator Expressions & Iterators",
        "accent_color": COLOR_PYTHON,
        "playlist_key": "python_longform",
        "tags": [
            "Python", "Python List Comprehensions", "Python Generators", "Iterators",
            "Python Tutorial", "Memory Optimization", "Python enumerate", "Python zip",
            "Clean Code Python", "Python Yield"
        ],
        "slides": [
            {
                "title": "Welcome to Day 3: Modern Iteration & Comprehensions",
                "bullets": [
                    "Day 3 of our 60-day engineering bootcamp: Mastering Pythonic iteration patterns.",
                    "Why traditional C-style index loops create fragile, slow, and unreadable code.",
                    "Today's roadmap: List comprehensions, memory-efficient generators, zip, and enumerate."
                ],
                "card_type": "code",
                "filename": "day03_intro.py",
                "code": "# Python Day 3: Modern Iteration Engine\\n# Transform raw data streams with zero boilerplate\\n\\nraw_data = [12, 45, 68, 93, 104, 150]\\nprocessed = [x * 2 for x in raw_data if x % 2 == 0]\\nprint(f'Even numbers doubled: {processed}')",
                "speech": (
                    "Welcome to Day 3 of our 60-Day Python Masterclass! Today, we leave behind clumsy, traditional "
                    "index loops and master Python's most iconic feature: comprehensions and generators. "
                    "In most languages, iterating over collections requires managing counters and bounds manually. "
                    "Python treats iteration as a first-class stream pipeline. By the end of this masterclass, "
                    "you will write code that runs up to fifty percent faster in CPython while reducing memory "
                    "consumption from gigabytes down to a few kilobytes."
                )
            },
            {
                "title": "The Death of C-Style Index Loops: Use enumerate()",
                "bullets": [
                    "Anti-pattern: Using range(len(arr)) to access indices creates unnecessary indirection.",
                    "The enumerate() built-in returns a lazy tuple pair containing index and element.",
                    "Clean tuple unpacking eliminates out-of-bounds index errors entirely."
                ],
                "card_type": "split",
                "bad_code": "# ❌ ROOKIE: Index Indirection\\nnames = ['Alice', 'Bob', 'Charlie']\\nfor i in range(len(names)):\\n    print(f'{i}: {names[i]}')\\n# Clunky, prone to index errors!",
                "good_code": "# ✅ PRO FIX: Pythonic enumerate\\nnames = ['Alice', 'Bob', 'Charlie']\\nfor idx, name in enumerate(names, start=1):\\n    print(f'{idx}: {name}')\\n# Clean, idiomatic & faster!",
                "speech": (
                    "Let's start by killing the single most common habit among beginners coming from C or Java: "
                    "writing for i in range of length of array. When you do this, Python must compute the length, "
                    "allocate a range iterator, and perform index subscript lookups on every single step. "
                    "Instead, use Python's built-in enumerate function. Enumerate yields a pair containing the counter "
                    "and the object itself. You can even pass start equals one to match human-readable numbering, "
                    "producing clean, readable code with zero indexing overhead."
                )
            },
            {
                "title": "Parallel Stream Processing with zip() and zip_longest()",
                "bullets": [
                    "zip(*iterables) aggregates elements from each iterator into tuples.",
                    "Iterates lazily, stopping immediately when the shortest input iterable is exhausted.",
                    "itertools.zip_longest allows padding shorter sequences with custom fill values."
                ],
                "card_type": "code",
                "filename": "parallel_zip.py",
                "code": "from itertools import zip_longest\\n\\nusers = ['Dev', 'Priya', 'Rohan']\\nscores = [98, 94]\\n\\n# Standard zip stops at shortest length\\npaired = list(zip(users, scores))  # [('Dev', 98), ('Priya', 94)]\\n\\n# zip_longest fills missing values safely\\nsafe_pairs = list(zip_longest(users, scores, fillvalue=0))",
                "speech": (
                    "Next, let's explore parallel stream aggregation. When you have two related lists, such as user names "
                    "and test scores, never loop with an index counter to access both lists. Use the zip built-in. "
                    "Zip pairs elements side-by-side until the shortest iterable runs out. If your lists have unequal "
                    "lengths and you cannot afford to drop data, import zip longest from itertools. You can specify a "
                    "fill value such as zero or None, ensuring complete data integrity across all stream pipelines."
                )
            },
            {
                "title": "Anatomy of a List Comprehension",
                "bullets": [
                    "Mathematical set-builder notation: [expression for item in iterable if condition].",
                    "Executes at C-speed inside CPython by pre-allocating memory and avoiding bytecode loops.",
                    "Replaces multi-line loop initialization and append calls with a single readable expression."
                ],
                "card_type": "code",
                "filename": "comprehension_anatomy.py",
                "code": "# 1. Multi-line Imperative Loop\\nsquares = []\\nfor x in range(10):\\n    if x % 2 == 0:\\n        squares.append(x ** 2)\\n\\n# 2. Declarative List Comprehension\\nsquares_fast = [x ** 2 for x in range(10) if x % 2 == 0]\\n# [0, 4, 16, 36, 64]",
                "speech": (
                    "Now let's examine the anatomy of a list comprehension. A comprehension consists of three parts: "
                    "the transformation expression, the iteration loop, and the optional filtering condition. "
                    "Beyond syntax aesthetics, list comprehensions are dramatically faster than imperative loops. "
                    "In an imperative loop, Python must repeatedly look up the append attribute, build a method call "
                    "frame, and resize the list dynamically. A list comprehension executes specialized C-level bytecode "
                    "instructions, resulting in an immediate twenty to forty percent performance boost."
                )
            },
            {
                "title": "Dictionary & Set Comprehensions: Instant Unique Maps",
                "bullets": [
                    "Dict Comprehension: {key_expr: val_expr for item in iterable if condition}.",
                    "Set Comprehension: {expr for item in iterable} guarantees unique deduplicated items.",
                    "Ideal for building instant inverted indexes and fast in-memory lookup caches."
                ],
                "card_type": "code",
                "filename": "dict_set_comp.py",
                "code": "users = [{'id': 101, 'role': 'admin'}, {'id': 102, 'role': 'user'}]\\n\\n# Create instant O(1) lookup table by ID\\nuser_map = {u['id']: u['role'] for u in users}\\n# {101: 'admin', 102: 'user'}\\n\\n# Set comprehension: Unique roles\\nunique_roles = {u['role'] for u in users}\\n# {'admin', 'user'}",
                "speech": (
                    "The comprehension syntax isn't limited to lists; you can apply it to dictionaries and sets as well. "
                    "By using curly braces with a key-value colon syntax, you create dictionary comprehensions. "
                    "This is the industry standard pattern for converting database query records into instant in-memory "
                    "lookup tables indexed by primary key. Similarly, using curly braces without a colon builds a set "
                    "comprehension, automatically deduplicating values and providing constant O of one membership lookups."
                )
            },
            {
                "title": "The Memory Catastrophe: List vs Generator Expression",
                "bullets": [
                    "List Comprehension: Generates ALL elements immediately in RAM (Eager evaluation).",
                    "Generator Expression: Yields elements one at a time on demand (Lazy evaluation).",
                    "Processing 10 million records: List consumes 800 MB; Generator consumes 128 BYTES!"
                ],
                "card_type": "memory",
                "speech": (
                    "Here is where architectural decisions make or break production applications. When you use square "
                    "brackets, Python evaluates every single element upfront and stores the entire array in RAM. "
                    "If you are processing ten million database rows, a list comprehension will consume nearly a gigabyte "
                    "of RAM and trigger operating system swapping. By simply replacing the square brackets with round "
                    "parentheses, you create a generator expression. A generator stores zero data; it produces elements "
                    "on the fly, consuming only one hundred and twenty-eight bytes of memory regardless of data size."
                )
            },
            {
                "title": "Deep Dive: How Generator Functions & yield Work",
                "bullets": [
                    "The yield keyword pauses execution, saves stack state, and returns a value to the caller.",
                    "Resuming the generator picks up execution exactly where it left off on next().",
                    "Implements the producer-consumer pattern natively without multithreading locks."
                ],
                "card_type": "code",
                "filename": "generator_yield.py",
                "code": "def stream_large_dataset(limit):\\n    current = 0\\n    while current < limit:\\n        yield current ** 2\\n        current += 1\\n\\n# Consumes items on-demand\\ngen = stream_large_dataset(1_000_000)\\nprint(next(gen))  # 0\\nprint(next(gen))  # 1\\nprint(next(gen))  # 4",
                "speech": (
                    "Let's look under the hood of the yield keyword. When a function contains yield, Python flags it as a "
                    "generator factory. Calling the function does not execute the body; instead, it returns a generator "
                    "object. When next is invoked, Python runs the code until it hits yield, emits the value, and freezes "
                    "the function's stack frame in memory. When called again, execution resumes seamlessly from the frozen "
                    "state. This enables streaming multi-gigabyte log files through processing pipelines without memory errors."
                )
            },
            {
                "title": "The Python Iterator Protocol: __iter__ and __next__",
                "bullets": [
                    "Iterable: Any object implementing __iter__() that returns an iterator instance.",
                    "Iterator: An object implementing __next__() that yields values until raising StopIteration.",
                    "Every for-loop in Python is syntactic sugar over this two-method handshake protocol."
                ],
                "card_type": "code",
                "filename": "iterator_protocol.py",
                "code": "class CountUpTo:\\n    def __init__(self, max_val):\\n        self.max_val = max_val\\n        self.current = 1\\n\\n    def __iter__(self):\\n        return self\\n\\n    def __next__(self):\\n        if self.current > self.max_val:\\n            raise StopIteration\\n        val = self.current\\n        self.current += 1\\n        return val",
                "speech": (
                    "Every single loop in Python relies on the formal Iterator Protocol. This protocol consists of two "
                    "dunder methods: double underscore iter and double underscore next. An iterable is anything that "
                    "can return an iterator. An iterator must provide the next method, which returns the next item or "
                    "raises StopIteration when the stream ends. When you write a for loop, Python secretly calls iter "
                    "on your collection and repeatedly invokes next inside an implicit try-except block."
                )
            },
            {
                "title": "The Rookie Trap: Quadruple Nested Comprehensions",
                "bullets": [
                    "Writing 3 or 4 nested loops inside a single comprehension destroys maintainability.",
                    "Violates PEP 20: 'Readability counts' and 'Flat is better than nested'.",
                    "Debugging syntax errors or tracing runtime exceptions becomes nearly impossible."
                ],
                "card_type": "split",
                "bad_code": "# ❌ ROOKIE TRAP: Unreadable Nightmare\\nmatrix = [[[1, 2], [3]], [[4, 5]]]\\nflat = [x for layer in matrix for row in layer for x in row if x % 2 == 0]\\n# Nobody on your team can parse this!",
                "good_code": "# ✅ PRO FIX: Modular Generator Pipeline\\ndef flatten_layers(matrix):\\n    for layer in matrix:\\n        for row in layer:\\n            yield from row\\n\\nflat = [x for x in flatten_layers(matrix) if x % 2 == 0]\\n# Clear, debuggable, and maintainable!",
                "speech": (
                    "Now let's examine a dangerous anti-pattern: writing quadruple nested list comprehensions. "
                    "Just because Python allows you to pack three for-loops and multiple conditional filters into "
                    "one line does not mean you should. When production crashes, deciphering a complex one-liner "
                    "wastes precious engineering hours. The professional solution is to extract the nested unfolding "
                    "logic into a dedicated generator function using yield from, and keep the final comprehension "
                    "clean, readable, and focused on business transformations."
                )
            },
            {
                "title": "Bytecode Disassembly: Why Comprehensions Win",
                "bullets": [
                    "Using Python's dis module reveals bytecode execution instructions.",
                    "Traditional loops repeatedly execute LOAD_FAST, LOAD_METHOD, and CALL_METHOD.",
                    "Comprehensions use dedicated LIST_APPEND opcodes that bypass method resolution."
                ],
                "card_type": "code",
                "filename": "disassembly_test.py",
                "code": "import dis\\n\\ndef loop_version():\\n    out = []\\n    for i in range(100):\\n        out.append(i)\\n\\ndef comp_version():\\n    return [i for i in range(100)]\\n\\n# comp_version uses specialized LIST_APPEND opcode!\\ndis.dis(comp_version)",
                "speech": (
                    "Why are list comprehensions faster under the hood? Let's inspect the CPython bytecode using the "
                    "standard dis module. In a manual loop with append, Python executes LOAD METHOD and CALL METHOD on "
                    "every iteration, performing full attribute lookups. In contrast, a list comprehension compiles "
                    "into specialized bytecode that uses the LIST APPEND opcode. This opcode directly pushes elements "
                    "onto the C array without invoking Python method dispatch, giving you free performance gains."
                )
            },
            {
                "title": "Production Pipeline: Chaining Generator Stages",
                "bullets": [
                    "Build streaming data pipelines similar to UNIX pipes: cat | grep | awk.",
                    "Chain generator expressions to parse, validate, and transform data line by line.",
                    "Guarantees near-zero RAM usage even when streaming a 50 GB CSV file."
                ],
                "card_type": "code",
                "filename": "streaming_pipeline.py",
                "code": "# 1. Stream lines from disk (zero RAM)\\nlines = (line.strip() for line in open('server_logs.txt'))\\n\\n# 2. Filter 500 error logs\\nerrors = (line for line in lines if 'HTTP 500' in line)\\n\\n# 3. Extract IP addresses\\nip_addrs = (line.split()[0] for line in errors)\\n\\n# Pipeline executes ONLY when consumed!\\ntop_error_ip = next(ip_addrs)",
                "speech": (
                    "In enterprise software, the most powerful pattern is chaining generator stages together. "
                    "Think of this like UNIX command line pipes. We create a generator to stream raw lines from disk, "
                    "pipe that into a generator that filters for HTTP five hundred server errors, and pipe that into a "
                    "generator that extracts IP addresses. No data is read from disk until you pull elements from the "
                    "end of the pipeline. You can process a fifty gigabyte log file on a system with only two gigabytes of RAM."
                )
            },
            {
                "title": "Senior Trap: Late Binding Closures in Comprehensions",
                "bullets": [
                    "Functions defined inside loops or comprehensions bind variables by REFERENCE, not by value.",
                    "All closures end up sharing the final loop variable value when invoked later!",
                    "Pro fix: Bind default arguments (x=x) to capture the current state during creation."
                ],
                "card_type": "split",
                "bad_code": "# ❌ ROOKIE TRAP: Late Binding\\nfuncs = [lambda: i for i in range(3)]\\nprint([f() for f in funcs])\\n# Output: [2, 2, 2]! All share final i!",
                "good_code": "# ✅ PRO FIX: Default Arg Capture\\nfuncs = [lambda i=i: i for i in range(3)]\\nprint([f() for f in funcs])\\n# Output: [0, 1, 2]! Value frozen at creation!",
                "speech": (
                    "Here is a classic FAANG interview trap that catches even experienced engineers: late binding closures. "
                    "When you define lambda functions inside a list comprehension, Python does not freeze the variable's "
                    "value at that moment; it captures the variable name by reference. When you invoke the functions later, "
                    "every function looks up the variable and sees its final value, printing two, two, two! "
                    "To fix this, assign the variable as a default argument, freezing its current state when the function is born."
                )
            },
            {
                "title": "Clean Code Rules for Comprehensions",
                "bullets": [
                    "Rule 1: Maximum 2 clauses per comprehension (e.g., 1 for-clause and 1 if-clause).",
                    "Rule 2: Never use comprehensions for side-effects (e.g., [print(x) for x in arr] is bad practice).",
                    "Rule 3: If formatting requires more than two line breaks, refactor into a standard loop."
                ],
                "card_type": "code",
                "filename": "clean_rules.py",
                "code": "# ❌ Anti-pattern: Using comprehension purely for side effects\\n[do_network_call(u) for u in user_list]\\n\\n# ✅ Clean standard loop for actions\\nfor user in user_list:\\n    do_network_call(user)\\n\\n# ✅ Comprehensions exclusively for data transformation\\nactive_emails = [u.email for u in user_list if u.is_active]",
                "speech": (
                    "Let's review the enterprise clean code rules. Rule number one: limit your comprehensions to at "
                    "most two clauses. If you have two for-loops and two if-conditions, it belongs in a regular loop. "
                    "Rule number two: never use a comprehension solely for side effects. Writing a comprehension just "
                    "to call print or save to database wastes memory building a throwaway list. Comprehensions should be "
                    "reserved exclusively for transforming data from one representation into another."
                )
            },
            {
                "title": "Day 3 Coding Challenge: Flatten & Filter Matrix",
                "bullets": [
                    "Task: Given a ragged 2D matrix of user transaction amounts, extract all positive values.",
                    "Requirements: Single-line expression, O(n) time, and zero intermediate memory leaks.",
                    "Test your solution against edge cases including empty sub-lists and negative values."
                ],
                "card_type": "code",
                "filename": "day03_challenge.py",
                "code": "transactions = [\\n    [100, -20, 350],\\n    [],\\n    [-50, 420, 80],\\n    [-10]\\n]\\n\\n# YOUR TASK: One-line list comprehension\\n# Expected: [100, 350, 420, 80]\\nclean_tx = [val for row in transactions for val in row if val > 0]\\nprint(f'Clean Transactions: {clean_tx}')",
                "speech": (
                    "Here is your hands-on coding challenge for Day 3. You are provided with a ragged two-dimensional "
                    "matrix of user transaction amounts containing empty lists and negative chargebacks. "
                    "Your task is to write a single-line list comprehension that flattens the nested lists and filters "
                    "out all non-positive values, producing a clean, one-dimensional array. Pause the video and attempt "
                    "this now. The verified solution is displayed on your screen."
                )
            },
            {
                "title": "Day 3 Summary & Tomorrow's Roadmap",
                "bullets": [
                    "Key Takeaway 1: Use enumerate() for clean counters and zip() for parallel stream merging.",
                    "Key Takeaway 2: Choose generators over list comprehensions for large or unbounded datasets.",
                    "Tomorrow (Day 4): Functions, Scopes, Closures, Decorators & Python Stack Frames."
                ],
                "card_type": "code",
                "filename": "day03_summary.py",
                "code": "# Day 3 Key Takeaways:\\n# 1. enumerate() & zip() eliminate brittle indexing\\n# 2. Comprehensions execute at C-speed\\n# 3. Generators provide O(1) memory streaming\\n# 4. Watch out for late-binding closure traps!\\n\\nprint('Day 3 Complete! See you tomorrow at 10 AM!')",
                "speech": (
                    "That concludes Day 3 of our Python Masterclass! Today you mastered idiomatic iteration with "
                    "enumerate and zip, unlocked C-level execution speed with comprehensions, and discovered how "
                    "generator expressions achieve constant O of one memory efficiency. Remember to always respect "
                    "readability and avoid late binding traps. Tomorrow at 10 AM, we dive into functions, variable "
                    "scopes, closures, and the magic of decorators. Make sure you are subscribed to BharatBeacon, "
                    "and I will see you in Day 4!"
                )
            }
        ]
    },

    # =========================================================================
    # 2. JAVA DAY 3 MASTERCLASS (Target: 11 - 13 Minutes)
    # =========================================================================
    {
        "track": "java",
        "track_title": "JAVA MASTERCLASS",
        "episode_info": "DAY 03 OF 60",
        "title": "Java Day 3: Control Flow Mastery: Loops, Labeled Jumps & Modern Switch Expressions",
        "accent_color": COLOR_JAVA,
        "playlist_key": "java_longform",
        "tags": [
            "Java", "Java Tutorial", "Java Control Flow", "Java Switch",
            "Java Pattern Matching", "Learn Java", "Java Loops", "Clean Code Java",
            "Java 17", "Java 21"
        ],
        "slides": [
            {
                "title": "Welcome to Java Day 3: Modern Control Flow",
                "bullets": [
                    "Day 3 of our 60-day enterprise engineering bootcamp: Controlling execution pathways.",
                    "Moving beyond legacy Java 7 idioms to modern, safe Java 17 and 21 control flow structures.",
                    "Today's roadmap: Loop mechanics, labeled jumps, modern switch expressions, and pattern matching."
                ],
                "card_type": "code",
                "filename": "ControlFlowApp.java",
                "code": "public class ControlFlowApp {\\n    public static void main(String[] args) {\\n        System.out.println(\\\"Welcome to Day 3 of 60-Day Java Masterclass!\\\");\\n        // Today: Loops, Enhanced Iteration & Pattern Matching\\n    }\\n}",
                "speech": (
                    "Welcome to Day 3 of our 60-Day Java Masterclass! Today we master the circulatory system of "
                    "software engineering: control flow. While every developer knows basic if-else statements, "
                    "enterprise systems fail when loops introduce concurrency bugs or when verbose switch statements "
                    "suffer from accidental fall-through. Today, we will explore loop execution mechanics under the hood, "
                    "uncover the power of labeled break statements, and unlock the game-changing modern switch "
                    "expressions introduced in modern LTS versions of Java."
                )
            },
            {
                "title": "Loop Mechanics: Traditional vs Enhanced for-each",
                "bullets": [
                    "Traditional for-loop: Index-based iteration using loop counters and termination bounds.",
                    "Enhanced for-each loop: Syntactic sugar over the java.lang.Iterable interface.",
                    "Eliminates off-by-one errors and array index out of bounds exceptions."
                ],
                "card_type": "code",
                "filename": "LoopComparison.java",
                "code": "List<String> services = List.of(\\\"Auth\\\", \\\"Billing\\\", \\\"Orders\\\");\\n\\n// 1. Traditional Index Loop\\nfor (int i = 0; i < services.size(); i++) {\\n    System.out.println(services.get(i));\\n}\\n\\n// 2. Enhanced For-Each (Modern & Safe)\\nfor (String service : services) {\\n    System.out.println(service);\\n}",
                "speech": (
                    "Let's compare the traditional index-based for loop with the enhanced for-each loop. "
                    "In the traditional loop, you manage an integer counter, check boundary conditions, and call get "
                    "repeatedly. If you make a simple comparison typo, your code crashes with an ArrayIndexOutOfBoundsException. "
                    "The enhanced for-each loop, introduced in Java 5, eliminates manual indexing completely. "
                    "It works uniformly across both native arrays and any collection implementing the Iterable interface, "
                    "resulting in cleaner, self-documenting code with zero boundary hazards."
                )
            },
            {
                "title": "Under The Hood: How for-each Uses java.util.Iterator",
                "bullets": [
                    "The Java compiler rewrites enhanced for-loops over collections into Iterator calls.",
                    "Invokes iterator(), hasNext(), and next() under the hood.",
                    "Keeps track of collection state and structural modifications in memory."
                ],
                "card_type": "code",
                "filename": "IteratorDecompile.java",
                "code": "// What the JVM Actually Compiles:\\nIterator<String> it = services.iterator();\\nwhile (it.hasNext()) {\\n    String service = it.next();\\n    System.out.println(service);\\n}",
                "speech": (
                    "Have you ever wondered what the Java compiler actually generates when you write an enhanced for loop? "
                    "If you decompile the bytecode, you will find that for any Collection object, the compiler transforms "
                    "your clean for-each statement into an explicit while loop utilizing java util Iterator. "
                    "It calls services dot iterator, checks hasNext before every iteration, and extracts the element with next. "
                    "Understanding this internal transformation is essential for diagnosing the most notorious exception in Java."
                )
            },
            {
                "title": "The Production Killer: ConcurrentModificationException",
                "bullets": [
                    "Modifying a collection directly while looping through it causes an instant crash.",
                    "The collection tracks changes via an internal modCount counter variable.",
                    "If modCount does not match the iterator's expectedModCount, the JVM throws an error!"
                ],
                "card_type": "split",
                "bad_code": "// ❌ ROOKIE TRAP: Crash in Production!\\nList<String> list = new ArrayList<>(List.of(\\\"A\\\", \\\"B\\\", \\\"C\\\"));\\nfor (String item : list) {\\n    if (item.equals(\\\"B\\\")) {\\n        list.remove(item); // CRASH!\\n    }\\n}\\n// Throws ConcurrentModificationException!",
                "good_code": "// ✅ PRO FIX: Use removeIf or Iterator\\nList<String> list = new ArrayList<>(List.of(\\\"A\\\", \\\"B\\\", \\\"C\\\"));\\n\\n// Solution 1: Clean Predicate (Java 8+)\\nlist.removeIf(item -> item.equals(\\\"B\\\"));\\n\\n// Solution 2: Explicit Iterator\\n// it.remove() syncs modCount correctly!",
                "speech": (
                    "Here is a rookie mistake that causes immediate crashes in production microservices: "
                    "trying to remove an item from a list while iterating over it in a for-each loop. "
                    "Every ArrayList maintains an internal variable named modCount that increments whenever elements are added or removed. "
                    "When the iterator detects that modCount differs from its expected count, it immediately throws a "
                    "ConcurrentModificationException to prevent data corruption. The industry-standard solution is to use "
                    "Collection dot removeIf with a lambda predicate, or call remove directly on the Iterator object itself."
                )
            },
            {
                "title": "The Forgotten Java Superpower: Labeled Break & Continue",
                "bullets": [
                    "Standard break only exits the innermost enclosing loop.",
                    "Labeled break (outerLoop: for (...)) allows breaking out of deeply nested structures cleanly.",
                    "Avoids messy boolean flag variables and deeply indented guard clauses."
                ],
                "card_type": "code",
                "filename": "LabeledJump.java",
                "code": "searchMatrix:\\nfor (int r = 0; r < matrix.length; r++) {\\n    for (int c = 0; c < matrix[r].length; c++) {\\n        if (matrix[r][c] == target) {\\n            System.out.println(\\\"Found at: \\\" + r + \\\", \\\" + c);\\n            break searchMatrix; // Exits BOTH loops instantly!\\n        }\\n    }\\n}",
                "speech": (
                    "Here is a powerful, yet frequently overlooked Java feature: labeled jump statements. "
                    "When working with multi-dimensional arrays or nested processing algorithms, a standard break statement "
                    "only terminates the innermost loop. Beginners often introduce clumsy boolean flags like found equals true "
                    "and repeat checks at every outer tier. By placing a label like searchMatrix followed by a colon before "
                    "the outer loop, you can execute break searchMatrix, instantly terminating all nested loop tiers in a single, "
                    "clean, and highly readable instruction."
                )
            },
            {
                "title": "The Evolution of switch: From C-Legacy to Modern Java",
                "bullets": [
                    "Java 1.0: Only primitive integers (byte, short, int, char).",
                    "Java 5: Added Enums. Java 7: Added Strings.",
                    "Java 14+: Modern Switch Expressions with arrow syntax and return values.",
                    "Java 17/21: Pattern Matching and Type Checking."
                ],
                "card_type": "memory",
                "speech": (
                    "The switch statement in Java has undergone a remarkable architectural evolution. In early Java, switch "
                    "could only evaluate basic integer primitives. Java five introduced Enums, and Java seven finally allowed "
                    "Strings. However, it still suffered from the error-prone legacy inherited from C, requiring explicit "
                    "break statements after every case. Starting with Java fourteen and refined in Java seventeen and twenty-one, "
                    "Java transformed switch into a modern, expressive functional construct capable of pattern matching and "
                    "returning values directly."
                )
            },
            {
                "title": "The Classic Trap: Accidental Fall-Through & Missing break",
                "bullets": [
                    "Traditional switch statements require explicit break statements.",
                    "Omitting break causes execution to fall through into subsequent case blocks silently.",
                    "A notorious source of critical security and financial logic bugs."
                ],
                "card_type": "split",
                "bad_code": "// ❌ ROOKIE TRAP: Fall-through Disaster\\nint tier = 1;\\nswitch (tier) {\\n    case 1:\\n        grantSilverAccess();\\n        // MISSING BREAK!\\n    case 2:\\n        grantAdminAccess(); // EXECUTED!\\n        break;\\n}",
                "good_code": "// ✅ PRO FIX: Modern Switch Arrow Syntax\\nint tier = 1;\\nswitch (tier) {\\n    case 1 -> grantSilverAccess();\\n    case 2 -> grantAdminAccess();\\n    default -> denyAccess();\\n}\\n// Zero fall-through! Impossible to leak!",
                "speech": (
                    "Look at this catastrophic bug caused by traditional switch fall-through. If an engineer forgets a "
                    "single break statement after case one, the JVM does not stop; it falls straight through and executes "
                    "case two as well, mistakenly granting admin access to a basic user! This has caused severe security "
                    "vulnerabilities across the industry. With modern switch arrow syntax, fall-through is impossible by design. "
                    "Only the matched branch executes, completely eliminating this class of runtime errors."
                )
            },
            {
                "title": "Switch Expressions: Returning Values & the yield Keyword",
                "bullets": [
                    "Modern switch can be used as an expression that produces a value directly.",
                    "Assign results directly to variables: String res = switch(status) { ... }.",
                    "The yield keyword is used when a case block requires multiple preparatory statements."
                ],
                "card_type": "code",
                "filename": "SwitchYield.java",
                "code": "int statusCode = 404;\\n\\nString message = switch (statusCode) {\\n    case 200 -> \\\"OK\\\";\\n    case 404 -> \\\"Not Found\\\";\\n    case 500 -> \\\"Internal Server Error\\\";\\n    default  -> {\\n        logUnknownStatus(statusCode);\\n        yield \\\"Unknown Error Code\\\"; // Yields value from block\\n    }\\n};",
                "speech": (
                    "In modern Java, switch is not just a statement; it is an expression that yields a value. "
                    "Notice how we assign the output of the switch directly to the message variable. There is no need to "
                    "declare an empty variable beforehand and assign it across multiple branches. If a specific case requires "
                    "multiple statements, such as logging or validation, wrap the branch in curly braces and use the yield keyword. "
                    "Yield returns the computed value from that block while maintaining clean expression syntax."
                )
            },
            {
                "title": "Compiler Exhaustiveness: No More Missing Defaults",
                "bullets": [
                    "When using switch expressions with Enums or Sealed Classes, the compiler verifies all cases.",
                    "If you add a new Enum constant, your code fails to compile until all switches handle it!",
                    "Eliminates silent runtime errors when business models expand."
                ],
                "card_type": "code",
                "filename": "ExhaustiveSwitch.java",
                "code": "enum Priority { LOW, MEDIUM, HIGH, CRITICAL }\\n\\nint slaHours = switch (priority) {\\n    case LOW -> 48;\\n    case MEDIUM -> 24;\\n    case HIGH -> 8;\\n    case CRITICAL -> 1;\\n    // No default needed! Compiler verifies exhaustiveness\\n};",
                "speech": (
                    "One of the greatest benefits of modern switch expressions is compiler-enforced exhaustiveness. "
                    "When switching over an Enum or a sealed class hierarchy, the Java compiler verifies that every single "
                    "possible case is accounted for. If a teammate adds a new CRITICAL value to the Priority enum in the future, "
                    "the project will refuse to compile until every switch expression handles that new case. This moves bug "
                    "detection from late-night production outages directly into compile-time verification."
                )
            },
            {
                "title": "Java 21 Pattern Matching: Type Inspection & Casting",
                "bullets": [
                    "Replaces ugly chains of if (obj instanceof String) followed by manual casting.",
                    "Combines type testing and variable extraction into a single atomic branch.",
                    "Supports null checking directly as a distinct case branch."
                ],
                "card_type": "code",
                "filename": "PatternMatchingSwitch.java",
                "code": "static String formatObject(Object obj) {\\n    return switch (obj) {\\n        case null              -> \\\"Null Object\\\";\\n        case Integer i         -> String.format(\\\"Integer: %,d\\\", i);\\n        case Long l            -> String.format(\\\"Long: %,d L\\\", l);\\n        case String s          -> \\\"String: \\\" + s.trim();\\n        case List<?> list      -> \\\"List of size \\\" + list.size();\\n        default                -> obj.toString();\\n    };\\n}",
                "speech": (
                    "With Java twenty-one, switch expressions gained full Pattern Matching capabilities. In older versions, "
                    "handling generic objects required chaining multiple if-statements, calling instanceof, and manually casting "
                    "the variable on the very next line. With pattern matching, you inspect the type and bind it to a typed "
                    "variable in a single step. Furthermore, modern switch handles null directly as an explicit case branch, "
                    "preventing unexpected NullPointerExceptions before your business logic even runs."
                )
            },
            {
                "title": "Guarded Patterns: Adding 'when' Conditions",
                "bullets": [
                    "Add boolean refinements to pattern matches using the 'when' keyword.",
                    "Allows matching specific data values alongside type inspections.",
                    "Keeps business logic declarative, flat, and free of nested if-statements."
                ],
                "card_type": "code",
                "filename": "GuardedPatterns.java",
                "code": "static String evaluateTransaction(Object tx) {\\n    return switch (tx) {\\n        case Integer amount when amount > 100_000 -> \\\"⚠️ High-Value Alert\\\";\\n        case Integer amount when amount > 0       -> \\\"Normal Payment\\\";\\n        case Integer amount                      -> \\\"Zero or Negative\\\";\\n        case String note when note.isBlank()     -> \\\"Empty Memo\\\";\\n        default                                  -> \\\"Standard Item\\\";\\n    };\\n}",
                "speech": (
                    "To make pattern matching even more expressive, Java introduced guarded patterns using the when keyword. "
                    "A guarded pattern allows you to append conditional business checks directly to your type pattern. "
                    "Notice how we can match an Integer and check whether its value exceeds one hundred thousand in the same line. "
                    "This replaces deeply nested if-else structures with flat, declarative decision tables that are easy to "
                    "audit, benchmark, and maintain."
                )
            },
            {
                "title": "Bytecode Internals: tableswitch vs lookupswitch",
                "bullets": [
                    "The JVM compiles switch statements into two distinct bytecodes.",
                    "tableswitch: Used for dense integer ranges; executes in O(1) jump table lookup time.",
                    "lookupswitch: Used for sparse cases; executes binary search in O(log n) time."
                ],
                "card_type": "memory",
                "speech": (
                    "Let's look at the JVM execution engine. When Java compiles a switch statement, it generates one of two "
                    "specialized bytecodes: tableswitch or lookupswitch. If your cases are contiguous, like one, two, and three, "
                    "the JVM creates a tableswitch. A tableswitch is a direct jump table in memory that executes in constant O of "
                    "one time. If your case values are sparse, like ten, five hundred, and ten thousand, the JVM generates a "
                    "lookupswitch, which sorts the keys and performs binary search in logarithmic time."
                )
            },
            {
                "title": "Top Senior Java Interview Trap: Null in Traditional Switch",
                "bullets": [
                    "In traditional switch statements, passing a null variable throws NullPointerException instantly.",
                    "It fails before any case is evaluated, even if a default branch exists!",
                    "In modern switch, explicitly declaring case null handles null references gracefully."
                ],
                "card_type": "split",
                "bad_code": "// ❌ TRADITIONAL SWITCH: Instant NPE\\nString str = null;\\nswitch (str) {\\n    case \\\"A\\\": System.out.println(\\\"A\\\"); break;\\n    default: System.out.println(\\\"Def\\\");\\n}\\n// Throws NullPointerException BEFORE default!",
                "good_code": "// ✅ MODERN JAVA 21: Safe Null Case\\nString str = null;\\nswitch (str) {\\n    case null -> System.out.println(\\\"Safe Null\\\");\\n    case \\\"A\\\"  -> System.out.println(\\\"A\\\");\\n    default   -> System.out.println(\\\"Other\\\");\\n}\\n// Perfectly safe! Handles null explicitly!",
                "speech": (
                    "Here is a classic Java interview question: what happens if you pass a null String into a traditional "
                    "switch statement that has a default branch? Most junior engineers assume it triggers the default branch. "
                    "In reality, it immediately throws a NullPointerException because the JVM dereferences the object before "
                    "comparing case values. In modern Java twenty-one, you can write case null as an explicit branch, safely "
                    "intercepting null pointers without wrapping your switch in defensive if-checks."
                )
            },
            {
                "title": "Day 3 Hands-On Challenge: Refactor Legacy Validator",
                "bullets": [
                    "Task: Refactor a 6-tier nested if-else payment validator into modern Java 21 switch expressions.",
                    "Requirements: Handle null safety, type pattern matching, and transaction thresholds with 'when'.",
                    "Verify your solution against edge cases including zero amounts and invalid payload types."
                ],
                "card_type": "code",
                "filename": "PaymentChallenge.java",
                "code": "record Payment(String currency, double amount) {}\\n\\n// CHALLENGE: Modernize this dispatcher with Java 21 Switch\\nstatic String process(Object req) {\\n    return switch (req) {\\n        case null -> \\\"REJECTED: Null Request\\\";\\n        case Payment p when p.amount() <= 0 -> \\\"INVALID_AMOUNT\\\";\\n        case Payment p -> \\\"APPROVED: \\\" + p.currency() + \\\" \\\" + p.amount();\\n        default -> \\\"UNSUPPORTED_PAYLOAD\\\";\\n    };\\n}",
                "speech": (
                    "Here is your Day 3 hands-on engineering challenge. You are given a legacy payment routing system "
                    "burdened with deeply nested if-statements and manual casts. Your task is to refactor this logic into "
                    "a modern, clean Java twenty-one switch expression. You must handle null verification, record pattern "
                    "matching, and currency validation using guarded patterns. Pause the video and test your implementation. "
                    "The production-ready solution is displayed on your screen."
                )
            },
            {
                "title": "Day 3 Summary & Tomorrow's Roadmap",
                "bullets": [
                    "Key Takeaway 1: Use enhanced for-each for safety; remove elements via removeIf() to prevent CME.",
                    "Key Takeaway 2: Adopt modern switch expressions for exhaustiveness, value returns, and zero fall-through.",
                    "Tomorrow (Day 4): Methods, Parameter Passing Mechanics & JVM Call Stack Tracing."
                ],
                "card_type": "code",
                "filename": "Day03Summary.java",
                "code": "// Java Day 3 Key Takeaways:\\n// 1. Enhanced loops eliminate off-by-one errors\\n// 2. removeIf() prevents ConcurrentModificationException\\n// 3. Arrow switch eliminates fall-through bugs\\n// 4. Pattern matching with 'when' revolutionizes control flow\\n\\nSystem.out.println(\\\"Day 3 Complete! See you tomorrow at 12 PM!\\\");",
                "speech": (
                    "Congratulations on completing Day 3 of our Java Masterclass! Today we unlocked the true mechanics of "
                    "Java control flow. You learned how enhanced loops operate under the hood, how to eliminate "
                    "ConcurrentModificationExceptions, and how modern switch expressions bring pattern matching and "
                    "compiler exhaustiveness to your code. Tomorrow at 12 PM, we dive into methods, parameter passing mechanics, "
                    "and stack frame lifecycles. Subscribe to BharatBeacon, practice the code examples, and I will see you tomorrow!"
                )
            }
        ]
    },

    # =========================================================================
    # 3. MONGODB DAY 3 MASTERCLASS (Target: 11 - 13 Minutes)
    # =========================================================================
    {
        "track": "mongodb",
        "track_title": "MONGODB MASTERCLASS",
        "episode_info": "DAY 03 OF 60",
        "title": "MongoDB Day 3: Advanced Comparison, Logical Operators & Array Querying",
        "accent_color": COLOR_MONGO,
        "playlist_key": "mongodb_longform",
        "tags": [
            "MongoDB", "NoSQL", "MongoDB Tutorial", "MongoDB Query",
            "Database", "Learn MongoDB", "MongoDB Operators", "BSON", "Clean Code"
        ],
        "slides": [
            {
                "title": "Welcome to MongoDB Day 3: Query Operators",
                "bullets": [
                    "Day 3 of our 60-day database engineering bootcamp: Mastering MongoDB query language.",
                    "Moving beyond simple key-value lookups to complex multi-condition document filtering.",
                    "Today's roadmap: Comparison operators, range queries, logical gates, and array inspection."
                ],
                "card_type": "code",
                "filename": "day03_query_engine.js",
                "code": "// MongoDB Day 3: Query Operators Engine\\n// Efficient document filtration across millions of records\\n\\ndb.products.find({\\n    category: 'Electronics',\\n    price: { $gte: 100, $lte: 500 },\\n    inStock: true\\n});",
                "speech": (
                    "Welcome to Day 3 of our 60-Day MongoDB Masterclass! Yesterday we mastered fundamental CRUD operations. "
                    "Today, we take our database skills to the engineering level by exploring advanced query operators. "
                    "In real-world applications, you rarely fetch documents using simple equality. You must filter items "
                    "across price ranges, evaluate complex boolean conditions with AND, OR, and NOR, and query deep inside "
                    "nested arrays. Today, you will master the MongoDB query engine and learn how to write queries that "
                    "utilize indexes efficiently."
                )
            },
            {
                "title": "Comparison Operators Foundation: $gt, $gte, $lt, $lte",
                "bullets": [
                    "MongoDB provides prefix comparison operators: $gt (greater than), $gte, $lt, $lte, $ne.",
                    "Syntax: { field: { $operator: value } }.",
                    "Supports numbers, dates, timestamps, and string comparisons according to BSON collation."
                ],
                "card_type": "code",
                "filename": "comparison_operators.js",
                "code": "// Find active orders placed within the last 7 days\\nconst sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);\\n\\ndb.orders.find({\\n    status: { $ne: 'CANCELLED' },\\n    orderDate: { $gte: sevenDaysAgo },\\n    totalAmount: { $gt: 50 }\\n});",
                "speech": (
                    "Let's begin with comparison operators. In MongoDB, comparison operators always start with a dollar sign "
                    "and are passed as an embedded document. The core operators are dollar g-t for greater than, dollar g-t-e "
                    "for greater than or equal, dollar l-t for less than, dollar l-t-e for less than or equal, and dollar n-e "
                    "for not equal. These operators work seamlessly across numeric values, ISO timestamps, and strings. "
                    "When querying on indexed fields, range operators perform lightning-fast B-tree range scans."
                )
            },
            {
                "title": "Compound Range Queries: Combining Bounds Cleanly",
                "bullets": [
                    "Combine lower and upper bounds within a single field document: { price: { $gte: 20, $lte: 100 } }.",
                    "Allows the MongoDB query planner to execute a bounded index scan between min and max keys.",
                    "Never repeat the same field name as separate root keys; JavaScript objects overwrite duplicates!"
                ],
                "card_type": "split",
                "bad_code": "// ❌ ROOKIE TRAP: Overwritten Key!\\ndb.inventory.find({\\n    qty: { $gte: 10 },\\n    qty: { $lte: 50 } // OVERWRITES FIRST QTY!\\n});\\n// JavaScript keeps ONLY the last key!",
                "good_code": "// ✅ PRO FIX: Unified Range Object\\ndb.inventory.find({\\n    qty: {\\n        $gte: 10,\\n        $lte: 50\\n    }\\n});\\n// Executes a true bounded range scan!",
                "speech": (
                    "Here is a rookie trap that causes silent data leakage. In JSON and JavaScript, an object cannot have "
                    "duplicate keys. If you write quantity dollar gte ten, followed by a comma and quantity dollar lte fifty, "
                    "JavaScript overwrites the first key completely! The database only receives the second filter. "
                    "The correct, production-grade pattern is to combine both bounds inside a single object under the quantity "
                    "key. This allows the query engine to perform an efficient, single-pass bounded index range scan."
                )
            },
            {
                "title": "Set Membership: $in and $nin Mechanics",
                "bullets": [
                    "$in matches any document where the field equals ANY value in the specified array.",
                    "$nin matches documents where the field value does NOT exist in the array.",
                    "$in utilizes B-tree indexes effectively; $nin requires inspecting all non-matching index entries."
                ],
                "card_type": "code",
                "filename": "set_membership.js",
                "code": "// Find users in specific target cities\\ndb.users.find({\\n    city: { $in: ['Bengaluru', 'Mumbai', 'Hyderabad'] },\\n    role: { $nin: ['BANNED', 'SUSPENDED'] }\\n});",
                "speech": (
                    "When filtering for multiple acceptable values, avoid writing endless OR statements. Use the dollar in "
                    "operator instead. Dollar in accepts an array of values and matches any document where the field equals "
                    "any element in that list. Conversely, dollar n-i-n matches documents where the field is not in the list. "
                    "From a performance perspective, dollar in can jump directly to specific keys in a B-tree index, "
                    "making it significantly faster than unindexed multi-clause queries."
                )
            },
            {
                "title": "Querying Arrays: $all vs $in",
                "bullets": [
                    "$in on an array field: Matches if the array contains AT LEAST ONE of the target items.",
                    "$all on an array field: Matches ONLY if the array contains EVERY target item specified.",
                    "Crucial distinction for skill matching, tagging systems, and category filtration."
                ],
                "card_type": "code",
                "filename": "array_all_vs_in.js",
                "code": "// Candidate skills: ['Python', 'Docker', 'AWS', 'Kubernetes']\\n\\n// 1. $in: Matches candidates with ANY skill\\ndb.candidates.find({ skills: { $in: ['Python', 'Rust'] } });\\n\\n// 2. $all: Matches candidates with BOTH skills\\ndb.candidates.find({ skills: { $all: ['Docker', 'Kubernetes'] } });",
                "speech": (
                    "When querying array fields, beginners frequently confuse dollar in with dollar all. "
                    "If a document contains an array of skills, searching with dollar in will return the candidate if they "
                    "have Python OR Rust. If your job specification requires both Docker AND Kubernetes, dollar in is wrong. "
                    "You must use dollar all. Dollar all ensures that every single element specified in your query array exists "
                    "inside the document's array, regardless of order or additional elements."
                )
            },
            {
                "title": "Logical Operators: Implicit $and vs Explicit $and",
                "bullets": [
                    "Implicit $and: By default, multiple comma-separated fields in a query are evaluated as AND.",
                    "Explicit $and: Required ONLY when querying the SAME field with multiple expressions or operators.",
                    "Keeping queries clean reduces query parsing overhead on the database server."
                ],
                "card_type": "split",
                "bad_code": "// ❌ ROOKIE TRAP: Redundant Explicit $and\\ndb.users.find({\\n    $and: [\\n        { status: 'ACTIVE' },\\n        { age: { $gte: 21 } }\\n    ]\\n});\\n// Verbose and unnecessary nesting!",
                "good_code": "// ✅ PRO FIX: Clean Implicit $and\\ndb.users.find({\\n    status: 'ACTIVE',\\n    age: { $gte: 21 }\\n});\\n// Idiomatic, clean, and parsed instantly!",
                "speech": (
                    "Now let's examine logical operators. In MongoDB, you almost never need to write an explicit dollar and array. "
                    "By default, any comma-separated fields inside a query document are automatically evaluated with logical AND. "
                    "Writing an explicit dollar and with separate objects adds unnecessary parsing overhead and clutters your "
                    "codebase. The only scenario where explicit dollar and is required is when you must apply multiple complex "
                    "expressions or dollar-or branches targeting the exact same field."
                )
            },
            {
                "title": "Logical Disjunction: The $or and $nor Operators",
                "bullets": [
                    "$or takes an array of query clauses and matches if ANY clause evaluates to true.",
                    "$nor matches documents where EVERY clause in the array evaluates to false.",
                    "Performance tip: For $or to be fast, EACH branch should have its own supporting index."
                ],
                "card_type": "code",
                "filename": "logical_or.js",
                "code": "// Find VIP customers OR customers with high cart value\\ndb.customers.find({\\n    $or: [\\n        { tier: 'PLATINUM' },\\n        { totalSpend: { $gte: 10_000 } }\\n    ]\\n});",
                "speech": (
                    "When you need to match either of two different conditions across different fields, use dollar or. "
                    "Dollar or takes an array of query documents and returns any record satisfying at least one branch. "
                    "However, take note of an important database architecture principle: if you run a dollar or query and only "
                    "one branch has an index, MongoDB cannot use the index for the entire query! For maximum speed, make sure "
                    "each field inside the dollar or array has an appropriate supporting index."
                )
            },
            {
                "title": "Handling Dynamic Schemas: The $exists and $type Operators",
                "bullets": [
                    "Because MongoDB is schema-flexible, different documents may possess different fields.",
                    "$exists: { field: { $exists: true } } filters documents that possess the given key.",
                    "$type: Checks the BSON data type (e.g., 'string', 'number', 'array', 'objectId')."
                ],
                "card_type": "code",
                "filename": "exists_and_type.js",
                "code": "// Find documents that have a 'discountCode' field\\ndb.orders.find({\\n    discountCode: { $exists: true, $ne: null }\\n});\\n\\n// Audit documents where phone was mistakenly stored as string\\ndb.users.find({\\n    phoneNumber: { $type: 'string' }\\n});",
                "speech": (
                    "In a schema-flexible document store, fields might exist in some documents but be omitted from others. "
                    "MongoDB provides two essential operators for inspecting schema structure: dollar exists and dollar type. "
                    "Dollar exists true finds documents that have the field, while dollar exists false finds records where the "
                    "key was omitted. Dollar type allows you to audit your collection for data integrity, such as identifying "
                    "records where a legacy migration accidentally stored numbers as strings."
                )
            },
            {
                "title": "The Null Trap: Why { field: null } Matches Missing Fields!",
                "bullets": [
                    "Querying { status: null } matches documents where status is null AND documents where status is MISSING!",
                    "To match documents where the field is explicitly null, combine with $exists: true.",
                    "A frequent cause of unexpected query result counts in production."
                ],
                "card_type": "split",
                "bad_code": "// ❌ ROOKIE TRAP: Matches Missing Too!\\ndb.users.find({\\n    deletedAt: null\\n});\\n// Matches deletedAt: null AND missing deletedAt!",
                "good_code": "// ✅ PRO FIX: Explicit Null Verification\\ndb.users.find({\\n    deletedAt: { $exists: true, $type: 'null' }\\n});\\n// Matches ONLY documents with explicit null!",
                "speech": (
                    "Here is a tricky MongoDB interview question that catches even senior developers. If you query with "
                    "deletedAt colon null, what does MongoDB return? Most people assume it only returns documents where "
                    "deletedAt is explicitly set to null. In reality, MongoDB returns both documents with explicit null AND "
                    "every document where the deletedAt field does not exist at all! If you strictly want documents containing "
                    "an explicit null value, you must check dollar type equals null alongside dollar exists true."
                )
            },
            {
                "title": "Multi-Condition Array Matching: The $elemMatch Operator",
                "bullets": [
                    "Standard queries on arrays of sub-documents match conditions across DIFFERENT array elements.",
                    "$elemMatch guarantees that all specified conditions match within the SAME single element.",
                    "Essential for e-commerce carts, transaction line items, and nested audit logs."
                ],
                "card_type": "code",
                "filename": "elem_match.js",
                "code": "// Order with items: [{ sku: 'A', qty: 5 }, { sku: 'B', qty: 2 }]\\n\\n// ❌ Matches if ANY item is 'A' and ANY item has qty >= 5\\ndb.orders.find({ 'items.sku': 'A', 'items.qty': { $gte: 5 } });\\n\\n// ✅ Matches ONLY if the SAME item has sku 'A' AND qty >= 5!\\ndb.orders.find({\\n    items: { $elemMatch: { sku: 'A', qty: { $gte: 5 } } }\\n});",
                "speech": (
                    "When querying arrays of embedded sub-documents, dollar elemMatch is indispensable. "
                    "If you query an order's items array for sku A and quantity greater than five using dot notation, "
                    "MongoDB returns true if item one has sku A and item two has quantity five! The conditions were satisfied "
                    "by different elements. To enforce that the exact same item must satisfy both conditions, you must use "
                    "dollar elemMatch. Dollar elemMatch isolates the criteria to an individual element inside the array."
                )
            },
            {
                "title": "Query Plan Analysis with .explain('executionStats')",
                "bullets": [
                    "Never deploy a complex query to production without inspecting its execution stats.",
                    "COLLSCAN: Full collection scan (Slow, scans every document in RAM/Disk).",
                    "IXSCAN: Index scan (Fast, scans only indexed B-tree leaf nodes).",
                    "Ratio of totalDocsExamined to nReturned should ideally be close to 1:1."
                ],
                "card_type": "code",
                "filename": "explain_analysis.js",
                "code": "const stats = db.products.find({\\n    category: 'Electronics',\\n    price: { $gte: 100 }\\n}).explain('executionStats');\\n\\nprint(`Execution Stage: ${stats.executionStats.executionStages.stage}`);\\nprint(`Docs Examined:   ${stats.executionStats.totalDocsExamined}`);\\nprint(`Docs Returned:   ${stats.executionStats.nReturned}`);",
                "speech": (
                    "How do you know if your query is running efficiently? Always attach dot explain with executionStats. "
                    "The output reveals the exact execution stage chosen by the MongoDB query planner. If the stage says "
                    "COLLSCAN, the database had to read every single document in the collection. If it says IXSCAN, it "
                    "leveraged an index. Your primary metric to watch is totalDocsExamined compared to nReturned. In a well-indexed "
                    "production system, that ratio should be as close to one-to-one as possible."
                )
            },
            {
                "title": "BSON Type Comparison Order: Sorting Gotchas",
                "bullets": [
                    "When a field contains mixed data types, MongoDB compares them using a strict BSON hierarchy.",
                    "Order: MinKey < Null < Numbers < Strings < Objects < Arrays < BinData < ObjectId < Boolean.",
                    "Enforces consistent, deterministic sorting even across heterogeneous collections."
                ],
                "card_type": "memory",
                "speech": (
                    "Because MongoDB collections can hold diverse data types, how does it sort documents when a field contains "
                    "both numbers and strings? MongoDB defines a strict internal BSON type comparison hierarchy. "
                    "Null ranks lower than numbers; numbers rank lower than strings; strings rank lower than documents and arrays, "
                    "and booleans rank near the top. This ensures that every sort operation is completely deterministic, "
                    "preventing random ordering bugs when dealing with legacy or polymorphic data structures."
                )
            },
            {
                "title": "Clean Code Rules for MongoDB Queries",
                "bullets": [
                    "Rule 1: Always specify a projection mask to eliminate unnecessary bandwidth transfer.",
                    "Rule 2: Prefer $in over multiple chained $or statements on the same field.",
                    "Rule 3: Avoid leading wildcards in regex queries ($regex: /^prefix/ can use an index; /.*suffix/ cannot!)."
                ],
                "card_type": "code",
                "filename": "query_clean_rules.js",
                "code": "// ❌ Bad: Unbounded regex forces full collection scan\\ndb.users.find({ email: /.*@gmail.com$/ });\\n\\n// ✅ Good: Left-anchored regex leverages B-tree index\\ndb.users.find({ username: /^john_/ });\\n\\n// ✅ Good: Return only required fields\\ndb.users.find({ active: true }, { username: 1, email: 1, _id: 0 });",
                "speech": (
                    "Let's summarize our enterprise clean code rules for MongoDB queries. Rule number one: always project "
                    "only the fields you need to save network bandwidth. Rule number two: whenever possible, replace chains of "
                    "OR statements on the same field with a clean dollar in operator. Rule number three: never use leading "
                    "wildcards in regular expression queries. A left-anchored regex starting with a caret can use an index, "
                    "while a regex with leading wildcards forces a full collection scan across your entire cluster."
                )
            },
            {
                "title": "Day 3 Hands-On Challenge: Multi-Tier Product Filter",
                "bullets": [
                    "Task: Build a query finding all products in category 'Laptops' or 'Phones', priced between $500 and $1500.",
                    "Requirements: Must have at least 4.5 star rating, be currently in stock, and have tag 'Featured'.",
                    "Verify your query produces an index-friendly query plan using .explain()."
                ],
                "card_type": "code",
                "filename": "day03_mongo_challenge.js",
                "code": "// CHALLENGE SOLUTION: Multi-Tier Filter\\ndb.products.find({\\n    category: { $in: ['Laptops', 'Phones'] },\\n    price: { $gte: 500, $lte: 1500 },\\n    rating: { $gte: 4.5 },\\n    inStock: true,\\n    tags: 'Featured'\\n}, { name: 1, price: 1, rating: 1, _id: 0 });",
                "speech": (
                    "Here is your hands-on coding challenge for Day 3. You are building an e-commerce catalog search endpoint. "
                    "Your task is to write a single MongoDB query that finds products in either the Laptops or Phones categories, "
                    "with a price between five hundred and fifteen hundred dollars, a minimum rating of four point five, and "
                    "containing the Featured tag. Pause the video and write the query now. The optimal, indexed solution is "
                    "displayed on your screen."
                )
            },
            {
                "title": "Day 3 Summary & Tomorrow's Roadmap",
                "bullets": [
                    "Key Takeaway 1: Combine range operators inside a single field object to avoid key collisions.",
                    "Key Takeaway 2: Use $elemMatch when querying multiple conditions on array sub-documents.",
                    "Tomorrow (Day 4): Advanced Update Operators ($set, $inc, $push, $pull, upsert)."
                ],
                "card_type": "code",
                "filename": "day03_mongo_summary.js",
                "code": "// Day 3 Key Takeaways:\\n// 1. $gt, $gte, $lt, $lte for bounded range scans\\n// 2. $in outperforms unindexed $or\\n// 3. $elemMatch enforces single-element condition matching\\n// 4. Always verify with .explain('executionStats')\\n\\nprint('Day 3 Complete! See you tomorrow at 2 PM!');",
                "speech": (
                    "Congratulations on completing Day 3 of our MongoDB Masterclass! Today you mastered the core query "
                    "operators: comparison ranges, set membership with dollar in, array querying with dollar all and "
                    "dollar elemMatch, and query plan profiling with explain. Tomorrow at 2 PM, we dive into powerful update "
                    "operators including dollar set, dollar inc, array mutators like push and pull, and atomic upsert operations. "
                    "Subscribe to BharatBeacon, practice with your local MongoDB instance, and I will see you tomorrow!"
                )
            }
        ]
    },

    # =========================================================================
    # 4. SQL DAY 3 MASTERCLASS (Target: 11 - 13 Minutes)
    # =========================================================================
    {
        "track": "sql",
        "track_title": "SQL MASTERCLASS",
        "episode_info": "DAY 03 OF 60",
        "title": "SQL Day 3: Aggregations Mastery: GROUP BY, HAVING, COUNT & Execution Pipeline",
        "accent_color": COLOR_SQL,
        "playlist_key": "sql_longform",
        "tags": [
            "SQL", "SQL Tutorial", "GROUP BY", "HAVING", "Database",
            "Learn SQL", "SQL Aggregations", "COUNT vs COUNT(*)", "Clean Code", "PostgreSQL"
        ],
        "slides": [
            {
                "title": "Welcome to SQL Day 3: Aggregations & Grouping",
                "bullets": [
                    "Day 3 of our 60-day relational database engineering bootcamp: Summarizing and analyzing data.",
                    "Moving beyond row-level queries to analytical aggregations and group transformations.",
                    "Today's roadmap: Aggregate functions, GROUP BY mechanics, WHERE vs HAVING, and execution order."
                ],
                "card_type": "code",
                "filename": "day03_agg_intro.sql",
                "code": "-- SQL Day 3: Relational Aggregations Engine\\n-- Summarize millions of transactions into actionable business insights\\n\\nSELECT \\n    department_id,\\n    COUNT(*) AS total_employees,\\n    ROUND(AVG(salary), 2) AS avg_salary\\nFROM employees\\nGROUP BY department_id\\nHAVING COUNT(*) >= 5;",
                "speech": (
                    "Welcome to Day 3 of our 60-Day SQL Masterclass! In modern software and data engineering, "
                    "retrieving raw rows is only half the battle. High-value systems depend on analytical aggregations: "
                    "calculating total revenue, finding average latencies, detecting user churn, and summarizing data into "
                    "meaningful metrics. Today, we will master aggregate functions, dissect the exact mechanics of GROUP BY, "
                    "uncover the critical architectural difference between WHERE and HAVING, and explore the internal "
                    "pipeline that powers SQL query execution."
                )
            },
            {
                "title": "Scalar vs Aggregate Functions: The Dimensional Collapse",
                "bullets": [
                    "Scalar Function (e.g., UPPER, ROUND): Takes 1 row's value, returns 1 modified value (1-to-1).",
                    "Aggregate Function (e.g., SUM, AVG): Takes N row values, collapses them into 1 scalar summary (N-to-1).",
                    "Cannot mix raw non-aggregated columns with aggregate functions without GROUP BY."
                ],
                "card_type": "code",
                "filename": "scalar_vs_aggregate.sql",
                "code": "-- Scalar: Operates per row (100 rows in -> 100 rows out)\\nSELECT first_name, UPPER(last_name), ROUND(salary, 0) FROM employees;\\n\\n-- Aggregate: Collapses rows (100 rows in -> 1 scalar out)\\nSELECT \\n    COUNT(*) AS employee_count,\\n    SUM(salary) AS total_payroll,\\n    AVG(salary) AS mean_compensation\\nFROM employees;",
                "speech": (
                    "Let's establish the fundamental distinction between scalar and aggregate functions. "
                    "A scalar function, such as UPPER or ROUND, transforms individual values row by row. If you feed in a "
                    "hundred rows, you get a hundred rows back. An aggregate function, such as SUM, AVG, or COUNT, takes an "
                    "entire set of rows and collapses them into a single scalar summary. Because of this dimensional collapse, "
                    "you cannot arbitrarily mix individual column names with aggregate functions without grouping."
                )
            },
            {
                "title": "The Big 5 Aggregate Functions & NULL Mechanics",
                "bullets": [
                    "COUNT: Counts rows or non-null values. SUM: Computes numeric totals.",
                    "AVG: Calculates arithmetic mean. MIN & MAX: Finds boundary extremes.",
                    "Crucial rule: All aggregate functions (except COUNT(*)) silently IGNORE NULL values!"
                ],
                "card_type": "code",
                "filename": "null_aggregates.sql",
                "code": "-- Table with bonuses: [1000, 2000, NULL, NULL]\\nSELECT \\n    COUNT(*) AS total_rows,       -- Returns 4\\n    COUNT(bonus) AS bonus_count,  -- Returns 2 (Ignores NULLs!)\\n    AVG(bonus) AS avg_bonus       -- (1000 + 2000) / 2 = 1500!\\n                                  -- NOT divided by 4!\\nFROM sales_reps;",
                "speech": (
                    "The five core SQL aggregate functions are COUNT, SUM, AVG, MIN, and MAX. However, here is the golden rule "
                    "that every database engineer must memorize: all aggregate functions, with the sole exception of COUNT star, "
                    "completely ignore NULL values! Look at the sales reps example on your screen. If four reps exist but two have "
                    "a NULL bonus, AVG bonus divides the sum by two, not four! If you want NULLs treated as zero, you must "
                    "wrap the column in COALESCE bonus comma zero."
                )
            },
            {
                "title": "The #1 SQL Interview Trap: COUNT(*) vs COUNT(column)",
                "bullets": [
                    "COUNT(*): Counts total rows returned by the query, regardless of NULLs or duplicate values.",
                    "COUNT(column_name): Counts ONLY rows where column_name is NOT NULL.",
                    "COUNT(DISTINCT column_name): Counts unique non-null occurrences."
                ],
                "card_type": "split",
                "bad_code": "-- ❌ ROOKIE TRAP: Miscounting Rows\\nSELECT COUNT(phone_number) AS total_users\\nFROM users;\\n-- Users with NULL phone numbers are MISSED!\\n-- Misrepresents total user count!",
                "good_code": "-- ✅ PRO FIX: Total vs Populated Metric\\nSELECT \\n    COUNT(*) AS total_users,\\n    COUNT(phone_number) AS verified_phones,\\n    COUNT(DISTINCT country) AS unique_countries\\nFROM users;\\n-- Accurately reflects both metrics!",
                "speech": (
                    "This is the single most tested question in database technical interviews: what is the difference between "
                    "COUNT star and COUNT of a column name? COUNT star counts every single row produced by the query table scan, "
                    "even if every column in that row is NULL. COUNT column name, by contrast, inspects the column and increments "
                    "its tally only when the value is NOT NULL. If you want the total population of a table, always use COUNT star. "
                    "Use COUNT column when you specifically want to count populated records."
                )
            },
            {
                "title": "How GROUP BY Works: The Memory Partitioning Phase",
                "bullets": [
                    "GROUP BY divides table rows into distinct buckets based on matching values in grouping keys.",
                    "The database engine creates an in-memory hash table or sorts rows by the grouping column.",
                    "Aggregate functions are then computed independently for each individual bucket."
                ],
                "card_type": "memory",
                "speech": (
                    "Let's look under the hood of the database engine during a GROUP BY operation. When you execute GROUP BY "
                    "department ID, the SQL engine partitions the rows in memory. It either sorts the table by department ID or "
                    "allocates an in-memory hash table where each unique department key points to an aggregation accumulator. "
                    "As the engine streams each row, it updates the running sum and count for that specific bucket. Once all rows "
                    "are processed, it outputs one summary row per unique group."
                )
            },
            {
                "title": "Multi-Column Grouping: Creating Hierarchical Data Cubes",
                "bullets": [
                    "Grouping by multiple columns: GROUP BY department, job_title.",
                    "Creates a unique bucket for every distinct COMBINATION of the specified columns.",
                    "Forms the foundation for multi-dimensional business reporting and pivot analysis."
                ],
                "card_type": "code",
                "filename": "multi_group.sql",
                "code": "SELECT \\n    region,\\n    product_category,\\n    COUNT(*) AS orders_count,\\n    SUM(order_total) AS total_revenue\\nFROM sales\\nGROUP BY region, product_category\\nORDER BY region, total_revenue DESC;",
                "speech": (
                    "You can group by as many columns as your reporting requires. When you specify GROUP BY region, product_category, "
                    "the database creates a distinct bucket for every unique combination of region and category. "
                    "North America Electronics is evaluated separately from North America Apparel, and separately from Europe Electronics. "
                    "This multi-column grouping forms the architectural basis for executive KPI dashboards, business intelligence "
                    "data cubes, and breakdown reports."
                )
            },
            {
                "title": "The Dreaded Syntax Error: Selecting Non-Grouped Columns",
                "bullets": [
                    "Error: 'column must appear in the GROUP BY clause or be used in an aggregate function'.",
                    "Why? If department 10 has 50 employees, which employee's first_name should the single row show?",
                    "Every column in SELECT must be either: 1) In GROUP BY, or 2) Inside an aggregate function."
                ],
                "card_type": "split",
                "bad_code": "-- ❌ ROOKIE TRAP: SQL Compilation Error!\\nSELECT \\n    department_id,\\n    first_name, -- ERROR! Which first_name?!\\n    AVG(salary)\\nFROM employees\\nGROUP BY department_id;",
                "good_code": "-- ✅ PRO FIX: Fully Aggregated Projection\\nSELECT \\n    department_id,\\n    COUNT(*) AS head_count,\\n    AVG(salary) AS mean_salary\\nFROM employees\\nGROUP BY department_id;\\n-- Perfectly deterministic & valid!",
                "speech": (
                    "Every developer encounters this famous error message: column must appear in the GROUP BY clause or be used "
                    "in an aggregate function. Why does SQL enforce this rule? Consider department ten. Department ten has fifty "
                    "employees with fifty different first names. If you ask the database to collapse department ten into a single "
                    "summary row, which employee's first name should it pick? The question is logically ambiguous. "
                    "Therefore, every column in your SELECT list must either be a grouping key or wrapped inside an aggregate function."
                )
            },
            {
                "title": "WHERE vs HAVING: The Architectural Barrier",
                "bullets": [
                    "WHERE filters individual rows BEFORE grouping and aggregation take place.",
                    "HAVING filters aggregated summary groups AFTER grouping has completed.",
                    "You CANNOT use aggregate functions like SUM() or COUNT() inside a WHERE clause!"
                ],
                "card_type": "split",
                "bad_code": "-- ❌ ROOKIE TRAP: Aggregate in WHERE!\\nSELECT department_id, COUNT(*)\\nFROM employees\\nWHERE COUNT(*) > 5 -- SYNTAX ERROR!\\nGROUP BY department_id;\\n-- Aggregates do NOT exist during WHERE phase!",
                "good_code": "-- ✅ PRO FIX: Proper Pipeline Separation\\nSELECT department_id, COUNT(*)\\nFROM employees\\nWHERE status = 'ACTIVE'       -- Filters rows first\\nGROUP BY department_id\\nHAVING COUNT(*) > 5;         -- Filters groups after\\n-- Clean, optimized execution!",
                "speech": (
                    "Now let's examine the most critical concept in SQL aggregations: WHERE versus HAVING. "
                    "A WHERE clause filters individual input rows before any grouping or aggregation takes place. "
                    "Because groups have not been created yet during the WHERE phase, writing WHERE COUNT star greater than five "
                    "is a severe syntax error. To filter aggregated results, you must use the HAVING clause. "
                    "HAVING executes after the GROUP BY phase, filtering the resulting summary groups based on aggregate calculations."
                )
            },
            {
                "title": "The True Query Execution Pipeline Order",
                "bullets": [
                    "SQL is written declaratively, but executes in a strict 6-stage pipeline under the hood:",
                    "1. FROM & JOIN (Identify tables) -> 2. WHERE (Filter rows) -> 3. GROUP BY (Partition buckets)",
                    "4. HAVING (Filter groups) -> 5. SELECT (Compute projections) -> 6. ORDER BY & LIMIT (Sort & Paginate)"
                ],
                "card_type": "memory",
                "speech": (
                    "To truly master SQL, you must understand the engine's internal execution pipeline. While you write SELECT "
                    "at the very top of your file, SELECT is actually one of the last stages executed! "
                    "First, the engine evaluates FROM and JOIN to identify the source tables. Second, it applies the WHERE clause "
                    "to discard unwanted rows. Third, it executes GROUP BY to partition the remaining data. Fourth, it evaluates "
                    "HAVING to filter the groups. Fifth, it computes the SELECT expressions and column aliases. Finally, it sorts "
                    "with ORDER BY and paginates with LIMIT."
                )
            },
            {
                "title": "Conditional Aggregation: The Power of SUM(CASE WHEN)",
                "bullets": [
                    "Transform row values into pivot columns using SUM(CASE WHEN ... THEN 1 ELSE 0 END).",
                    "Allows computing multiple specialized metrics in a single table scan.",
                    "Replaces multiple heavy queries with a single, high-performance aggregate projection."
                ],
                "card_type": "code",
                "filename": "conditional_aggregation.sql",
                "code": "SELECT \\n    department_id,\\n    COUNT(*) AS total_staff,\\n    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count,\\n    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,\\n    SUM(CASE WHEN salary > 100000 THEN 1 ELSE 0 END) AS high_earners\\nFROM employees\\nGROUP BY department_id;",
                "speech": (
                    "One of the most versatile techniques in professional SQL is conditional aggregation using CASE WHEN inside "
                    "aggregate functions. Suppose you need to report total staff, female staff, male staff, and high earners per "
                    "department. Beginners often write four separate queries and stitch them together in application code. "
                    "A senior engineer computes all four metrics in a single query by wrapping CASE statements inside SUM. "
                    "The database scans the table once, evaluates the conditional logic in memory, and returns the complete pivot."
                )
            },
            {
                "title": "Filtering with HAVING: Best Practices & Index Pushdown",
                "bullets": [
                    "Never put row-level filters in HAVING if they can be placed in WHERE.",
                    "Filtering with WHERE reduces the number of rows that must be sorted and aggregated in memory.",
                    "HAVING should strictly be reserved for conditions that evaluate aggregate functions."
                ],
                "card_type": "split",
                "bad_code": "-- ❌ POOR PRACTICE: Row filter in HAVING\\nSELECT department_id, AVG(salary)\\nFROM employees\\nGROUP BY department_id, country\\nHAVING country = 'IND'; -- Wastes RAM grouping all countries first!",
                "good_code": "-- ✅ PRO FIX: Pushdown Predicate to WHERE\\nSELECT department_id, AVG(salary)\\nFROM employees\\nWHERE country = 'IND'   -- Discards non-target rows instantly!\\nGROUP BY department_id;\\n-- 10x faster execution!",
                "speech": (
                    "Here is a crucial query optimization tip. Never place a filter in the HAVING clause if it can be evaluated "
                    "in the WHERE clause. If you want to analyze employees in India, putting country equals IND in the HAVING "
                    "clause forces the database to group employees from every country on earth before discarding them! "
                    "By placing country equals IND in the WHERE clause, the database filters the rows upfront using indexes, "
                    "passing only a fraction of the data into the expensive aggregation phase."
                )
            },
            {
                "title": "Grouping with ROLLUP & CUBE: Automatic Totals",
                "bullets": [
                    "GROUP BY ROLLUP(year, quarter) generates hierarchical subtotals and grand totals automatically.",
                    "CUBE generates subtotals for all possible cross-combinations of columns.",
                    "Eliminates messy UNION ALL chains when generating financial balance sheets."
                ],
                "card_type": "code",
                "filename": "rollup_cube.sql",
                "code": "-- Generate quarterly subtotals AND yearly grand total in 1 query\\nSELECT \\n    year,\\n    quarter,\\n    SUM(revenue) AS total_revenue\\nFROM corporate_earnings\\nGROUP BY ROLLUP(year, quarter)\\nORDER BY year, quarter;",
                "speech": (
                    "When building financial reports, you often need subtotals at each level plus an overall grand total. "
                    "In traditional SQL, engineers would write separate queries and stitch them together using UNION ALL. "
                    "Modern SQL engines provide the ROLLUP and CUBE extensions. Writing GROUP BY ROLLUP of year and quarter "
                    "automatically computes quarterly totals, calculates a yearly subtotal row, and emits a final grand total row, "
                    "saving dozens of lines of code and cutting database I-O in half."
                )
            },
            {
                "title": "Top FAANG SQL Interview Question: Finding Duplicates",
                "bullets": [
                    "Classic question: 'How do you identify duplicate email addresses in a 10-million row user table?'",
                    "Solution pattern: GROUP BY email HAVING COUNT(*) > 1.",
                    "Combine with window functions (ROW_NUMBER) to safely deduplicate rows."
                ],
                "card_type": "code",
                "filename": "find_duplicates.sql",
                "code": "-- Step 1: Identify all duplicate email addresses\\nSELECT \\n    email,\\n    COUNT(*) AS occurrence_count\\nFROM user_accounts\\nGROUP BY email\\nHAVING COUNT(*) > 1;\\n\\n-- Step 2: Extract full duplicate records\\n-- (Preview of Day 5: Window Functions)",
                "speech": (
                    "Here is a classic FAANG database interview problem: given a table with ten million customer accounts, "
                    "how do you identify all duplicate email addresses? The solution relies on grouping and the HAVING clause. "
                    "You execute SELECT email, COUNT star FROM user_accounts, GROUP BY email, and filter with HAVING COUNT star "
                    "greater than one. Any email that appears more than once will be returned alongside its occurrence count. "
                    "Mastering this pattern is a prerequisite for production database cleansing."
                )
            },
            {
                "title": "Day 3 Hands-On Challenge: Department Payroll Audit",
                "bullets": [
                    "Task: Write a query finding all departments with more than 3 active employees.",
                    "Calculate total payroll, minimum salary, and average salary rounded to 2 decimal places.",
                    "Order results by average salary in descending order; exclude employees with status 'ON_LEAVE'."
                ],
                "card_type": "code",
                "filename": "day03_sql_challenge.sql",
                "code": "-- CHALLENGE SOLUTION: Department Payroll Audit\\nSELECT \\n    department_id,\\n    COUNT(*) AS active_staff,\\n    SUM(salary) AS total_payroll,\\n    MIN(salary) AS entry_salary,\\n    ROUND(AVG(salary), 2) AS mean_compensation\\nFROM staff\\nWHERE employment_status = 'ACTIVE'\\nGROUP BY department_id\\nHAVING COUNT(*) > 3\\nORDER BY mean_compensation DESC;",
                "speech": (
                    "Here is your hands-on coding challenge for Day 3. You are tasked with auditing company payroll. "
                    "You must find all departments that employ more than three active staff members, compute their total "
                    "payroll, minimum salary, and average salary rounded to two decimal places, while excluding anyone on leave. "
                    "Finally, sort the results with the highest paying department at the top. Pause the video and write the query. "
                    "The production-ready SQL solution is displayed on your screen."
                )
            },
            {
                "title": "Day 3 Summary & Tomorrow's Roadmap",
                "bullets": [
                    "Key Takeaway 1: All aggregate functions except COUNT(*) silently ignore NULL values.",
                    "Key Takeaway 2: WHERE filters rows before grouping; HAVING filters aggregated groups after.",
                    "Tomorrow (Day 4): Relational Joins (INNER, LEFT, RIGHT, FULL, CROSS & Self Joins)."
                ],
                "card_type": "code",
                "filename": "day03_sql_summary.sql",
                "code": "-- Day 3 Key Takeaways:\\n-- 1. COUNT(*) for total rows; COUNT(col) for non-null count\\n-- 2. Non-grouped columns in SELECT cause syntax errors\\n-- 3. Push row filters to WHERE for index performance\\n-- 4. Execution order: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT\\n\\n-- Day 3 Complete! See you tomorrow at 6 PM!",
                "speech": (
                    "Congratulations on completing Day 3 of our SQL Masterclass! Today you mastered the relational aggregation "
                    "engine: understanding aggregate functions and NULL handling, avoiding non-grouped column syntax errors, "
                    "leveraging conditional aggregation with CASE WHEN, and internalizing the true SQL query execution pipeline. "
                    "Tomorrow at 6 PM, we dive into the heart of relational databases: JOINS, covering INNER, LEFT, RIGHT, FULL OUTER, "
                    "CROSS, and Self Joins. Subscribe to BharatBeacon, practice with your local SQL editor, and I will see you tomorrow!"
                )
            }
        ]
    }
]
'''

day3_data_file = CONTENT_DIR / "day3_data.py"
with open(day3_data_file, "w", encoding="utf-8") as f:
    f.write(day3_data_code)

print(f"Successfully generated {day3_data_file}")
