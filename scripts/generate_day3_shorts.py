# Day 3 - 20 Viral Tech Shorts (1 Short per Hour)

DAY3_SHORTS = [
    # 00:00 AM IST (Midnight Launch)
    {
        "hour_ist": 0,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Why range(len(x)) in Python is a Bad Habit #Shorts #Python",
        "badge": "PYTHON HABITS • DAY 3",
        "hook_text": "Why range(len(x)) is the worst Python habit you learned",
        "code": "# ❌ Clunky index lookup\nfor i in range(len(arr)):\n    print(arr[i])\n\n# ✅ Idiomatic enumerate\nfor idx, val in enumerate(arr, 1):\n    print(idx, val)",
        "caption": "Use enumerate() for clean counters!",
        "riddle_text": "Index Indirection vs Enumerate ⚡",
        "speech": (
            "Why is range of len of x the worst habit in Python? Because every loop iteration forces Python to perform "
            "costly index lookups and bounds checks. Use enumerate instead! It returns the index and item in a single lazy "
            "tuple pair. Day 3 Masterclass drops at 10 AM!"
        )
    },
    # 01:00 AM IST
    {
        "hour_ist": 1,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The Hidden Power of Labeled Breaks in Java #Shorts #Java",
        "badge": "JAVA SECRETS • DAY 3",
        "hook_text": "How to break out of nested loops in Java without boolean flags",
        "code": "outerLoop:\nfor (int r = 0; r < 10; r++) {\n    for (int c = 0; c < 10; c++) {\n        if (grid[r][c] == target)\n            break outerLoop; // Exits BOTH!\n    }\n}",
        "caption": "Break nested loops in 1 line with labels!",
        "riddle_text": "Labeled Jumps in Clean Java 🚀",
        "speech": (
            "How do you break out of deeply nested loops in Java without messy boolean flags? Use labeled break! "
            "Simply place a label name followed by a colon before your outer loop, and call break with that label. "
            "It terminates all loop tiers instantly in a single instruction. Master Java control flow at 12 PM today!"
        )
    },
    # 02:00 AM IST
    {
        "hour_ist": 2,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "Why $in Destroys Multiple $or Statements in MongoDB #Shorts #MongoDB",
        "badge": "MONGODB QUERY • DAY 3",
        "hook_text": "Why you should NEVER chain $or statements on the same field",
        "code": "// ❌ Slow, unindexed clauses\ndb.users.find({ $or: [{ role: 'A' }, { role: 'B' }] });\n\n// ✅ Fast B-Tree Index Jump\ndb.users.find({ role: { $in: ['A', 'B'] } });",
        "caption": "Always replace same-field $or with $in!",
        "riddle_text": "$in vs $or: B-Tree Index Duel ⚡",
        "speech": (
            "Why should you never chain multiple dollar-or statements on the same field in MongoDB? Because dollar-in "
            "is heavily optimized for B-tree index traversal, jumping directly to target keys, while unindexed dollar-or "
            "adds severe query parsing overhead. Master advanced MongoDB operators at 2 PM today!"
        )
    },
    # 03:00 AM IST
    {
        "hour_ist": 3,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "The #1 SQL Interview Trap: COUNT(*) vs COUNT(col) #Shorts #SQL",
        "badge": "SQL INTERVIEW • DAY 3",
        "hook_text": "The difference between COUNT(*) and COUNT(col) that fails interviews",
        "code": "-- Table has 4 rows, 2 are NULL\nSELECT COUNT(*)    -- Returns 4 (Counts all rows)\nSELECT COUNT(col)  -- Returns 2 (Ignores NULLs!)",
        "caption": "COUNT(col) ignores NULLs; COUNT(*) counts rows!",
        "riddle_text": "Did You Know COUNT(*) Ignores NULLs? 💡",
        "speech": (
            "What is the difference between COUNT star and COUNT column name that trips up ninety percent of developers? "
            "COUNT star counts every single row produced by the query. COUNT column name inspects each row and skips "
            "every NULL value! Master relational aggregations in our Day 3 SQL Masterclass at 6 PM!"
        )
    },
    # 04:00 AM IST
    {
        "hour_ist": 4,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "List vs Generator Memory Duel: 800MB vs 128 Bytes! #Shorts #Python",
        "badge": "PYTHON MEMORY • DAY 3",
        "hook_text": "How round brackets save 800MB of RAM in Python",
        "code": "# 10 Million items in RAM\nnums_list = [x for x in range(10_000_000)] # 800 MB!\n\n# Zero RAM Generator Stream\nnums_gen  = (x for x in range(10_000_000)) # 128 BYTES!",
        "caption": "Switch [] to () for instant zero-RAM streaming!",
        "riddle_text": "Square vs Round Brackets: 800MB saved 🤯",
        "speech": (
            "How does swapping square brackets for round parentheses save eight hundred megabytes of RAM? "
            "Square brackets create a list comprehension, loading all ten million elements into memory immediately. "
            "Round parentheses create a generator expression, calculating elements on demand using only one hundred "
            "and twenty-eight bytes! Full tutorial at 10 AM!"
        )
    },
    # 05:00 AM IST
    {
        "hour_ist": 5,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The ConcurrentModificationException Trap in Java #Shorts #Java",
        "badge": "JAVA BUG HUNT • DAY 3",
        "hook_text": "Why modifying a list in a for-each loop crashes Java instantly",
        "code": "// ❌ CRASH: modCount mismatch!\nfor (String s : list) {\n    if (s.equals(\"x\")) list.remove(s);\n}\n\n// ✅ PRO FIX: Predicate\nlist.removeIf(s -> s.equals(\"x\"));",
        "caption": "Always use removeIf() to prevent CME crashes!",
        "riddle_text": "Why does list.remove() crash inside loops? 💥",
        "speech": (
            "Why does modifying a list inside a for-each loop crash your Java application? Because Java tracks changes "
            "with an internal modCount variable. When the iterator detects modCount changed behind its back, it throws "
            "ConcurrentModificationException! Always use collection dot removeIf with a lambda instead."
        )
    },
    # 06:00 AM IST
    {
        "hour_ist": 6,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "Array Filtering in MongoDB: $all vs $in Explained #Shorts #MongoDB",
        "badge": "MONGODB ARRAYS • DAY 3",
        "hook_text": "The difference between $in and $all when querying MongoDB arrays",
        "code": "// Skills: ['Python', 'Docker', 'AWS']\n\n// $in: Matches candidates with ANY skill\n{ skills: { $in: ['Python', 'Rust'] } }\n\n// $all: Matches candidates with BOTH skills!\n{ skills: { $all: ['Python', 'Docker'] } }",
        "caption": "$in matches any element; $all requires all elements!",
        "riddle_text": "Any vs All: The Array Query Rule 🎯",
        "speech": (
            "What is the difference between dollar-in and dollar-all when querying MongoDB arrays? Dollar-in returns "
            "documents where at least one array element matches your query. Dollar-all guarantees that every single item "
            "in your query list exists in the document's array. Learn array query mastery at 2 PM today!"
        )
    },
    # 07:00 AM IST
    {
        "hour_ist": 7,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Why You CANNOT Filter Aggregates in a WHERE Clause #Shorts #SQL",
        "badge": "SQL RULES • DAY 3",
        "hook_text": "Why writing WHERE COUNT(*) > 5 throws a syntax error in SQL",
        "code": "-- ❌ SYNTAX ERROR!\nSELECT dept_id, COUNT(*)\nFROM employees\nWHERE COUNT(*) > 5;\n\n-- ✅ PRO FIX: Use HAVING!\nHAVING COUNT(*) > 5;",
        "caption": "WHERE filters rows before grouping; HAVING filters after!",
        "riddle_text": "WHERE vs HAVING: The Execution Barrier 🛡️",
        "speech": (
            "Why does writing WHERE COUNT star greater than five trigger a syntax error? Because SQL executes the WHERE "
            "clause before any grouping or aggregation takes place. Groups do not even exist yet! To filter aggregated "
            "summary groups, you must use the HAVING clause. Full SQL Masterclass drops at 6 PM!"
        )
    },
    # 08:00 AM IST
    {
        "hour_ist": 8,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Merge Lists Like a Pro with zip() and zip_longest() #Shorts #Python",
        "badge": "PYTHON STREAMS • DAY 3",
        "hook_text": "How to pair unequal lists in Python without losing data",
        "code": "from itertools import zip_longest\n\nnames  = ['Dev', 'Priya', 'Rohan']\nscores = [98, 95]\n\n# zip_longest prevents dropping 'Rohan'!\nlist(zip_longest(names, scores, fillvalue=0))",
        "caption": "Use zip_longest to avoid losing trailing data!",
        "riddle_text": "zip vs zip_longest: Zero Data Loss 🔗",
        "speech": (
            "How do you pair two lists in Python without losing trailing data when lengths differ? Standard zip terminates "
            "as soon as the shorter list ends. To preserve every record, import zip-longest from itertools and provide a "
            "clean fill value like zero or None. Level up your Python skills in our 10 AM Masterclass!"
        )
    },
    # 09:00 AM IST (Teaser for 10 AM Python Masterclass)
    {
        "hour_ist": 9,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Python Day 3 Masterclass Dropping in 1 Hour! (Comprehensions & Generators) #Shorts",
        "badge": "MASTERCLASS ALERT • 10 AM",
        "hook_text": "Python Day 3 Masterclass drops in exactly 60 minutes!",
        "code": "# Dropping at 10:00 AM IST:\n# 1. Enumerate & Zip Stream Pipelines\n# 2. List vs Generator Memory (800MB vs 128B)\n# 3. Disassembling Bytecode (LIST_APPEND)\n# 4. Late Binding Closure Traps & Fixes",
        "caption": "Full 12-Minute Python Masterclass at 10 AM!",
        "riddle_text": "Day 3 Dropping in 1 Hour! 🔔",
        "speech": (
            "Attention engineers! Day 3 of our 60-Day Python Masterclass drops in exactly one hour at 10 AM IST. "
            "Today we master list comprehensions, uncover how generators stream data using only one hundred bytes of RAM, "
            "and inspect CPython bytecode. Set your reminder and subscribe to BharatBeacon!"
        )
    },
    # 10:00 AM IST -> Python Masterclass published
    # 11:00 AM IST (Teaser for 12 PM Java Masterclass)
    {
        "hour_ist": 11,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Java Day 3 Masterclass Dropping in 1 Hour! (Modern Switch & Pattern Matching) #Shorts",
        "badge": "MASTERCLASS ALERT • 12 PM",
        "hook_text": "Java Day 3 Masterclass drops in exactly 60 minutes!",
        "code": "// Dropping at 12:00 PM IST:\n// 1. Enhanced Loops & Iterator Internals\n// 2. CME Prevention & modCount Sync\n// 3. Arrow Switch & Exhaustive Enums\n// 4. Java 21 Pattern Matching with 'when'",
        "caption": "Full 12-Minute Java Masterclass at 12 PM!",
        "riddle_text": "Day 3 Dropping in 1 Hour! 🔔",
        "speech": (
            "Our Java Day 3 Masterclass drops in exactly one hour at 12 PM IST! Today you will learn the internal "
            "mechanics of loop execution, labeled jumps, and unlock Java 21 pattern matching with modern switch expressions. "
            "Subscribe to BharatBeacon and join us at 12 PM!"
        )
    },
    # 12:00 PM IST -> Java Masterclass published
    # 01:00 PM IST (Teaser for 2 PM MongoDB Masterclass)
    {
        "hour_ist": 13,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "MongoDB Day 3 Masterclass Dropping in 1 Hour! (Advanced Query Operators) #Shorts",
        "badge": "MASTERCLASS ALERT • 2 PM",
        "hook_text": "MongoDB Day 3 Masterclass drops in exactly 60 minutes!",
        "code": "// Dropping at 2:00 PM IST:\n// 1. Compound Range Scans ($gt, $lte)\n// 2. $in vs $or Index Benchmarks\n// 3. The Null & Missing Field Trap\n// 4. Multi-Condition Array Matching with $elemMatch",
        "caption": "Full 12-Minute MongoDB Masterclass at 2 PM!",
        "riddle_text": "Day 3 Dropping in 1 Hour! 🔔",
        "speech": (
            "Our MongoDB Day 3 Masterclass goes live in exactly one hour at 2 PM IST! Today we master advanced query "
            "operators, analyze execution stats with dot explain, and solve the array sub-document matching problem with "
            "dollar elemMatch. Don't miss it!"
        )
    },
    # 02:00 PM IST -> MongoDB Masterclass published
    # 03:00 PM IST
    {
        "hour_ist": 15,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "The Late-Binding Closure Trap in Python Comprehensions #Shorts #Python",
        "badge": "FAANG GOTCHA • DAY 3",
        "hook_text": "The subtle lambda bug inside Python loops that breaks interviews",
        "code": "# ❌ Output: [2, 2, 2]! (Late binding)\nfuncs = [lambda: i for i in range(3)]\n\n# ✅ Output: [0, 1, 2]! (Default arg capture)\nfuncs = [lambda i=i: i for i in range(3)]",
        "caption": "Use default arg (i=i) to freeze closure values!",
        "riddle_text": "Why did all lambdas return 2? 🤯",
        "speech": (
            "Look at this subtle Python interview bug. When you define lambdas inside a loop, Python binds variables by "
            "reference, not by value! All lambdas share the final value, printing two, two, two! Fix it by capturing the "
            "variable as a default parameter, freezing its value at definition time."
        )
    },
    # 04:00 PM IST
    {
        "hour_ist": 16,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Why Modern Java 21 Switch Arrow Syntax Destroys Fall-Through #Shorts #Java",
        "badge": "MODERN JAVA • DAY 3",
        "hook_text": "How modern Java eliminated the infamous missing-break bug",
        "code": "// ❌ Accidental Fall-through\ncase 1: grantBasic(); // MISSING BREAK!\ncase 2: grantAdmin(); // LEAKS!\n\n// ✅ Modern Arrow Syntax: ZERO Fall-through\ncase 1 -> grantBasic();\ncase 2 -> grantAdmin();",
        "caption": "Arrow syntax makes fall-through impossible by design!",
        "riddle_text": "Clean Code in Java 21 🛡️",
        "speech": (
            "How did modern Java kill the single most dangerous bug in traditional switch statements? By introducing arrow "
            "syntax! Arrow syntax has zero fall-through by design. Only the matched branch executes, making it structurally "
            "impossible for permission leaks to occur. Write clean, safe Java code every day!"
        )
    },
    # 05:00 PM IST (Teaser for 6 PM SQL Masterclass)
    {
        "hour_ist": 17,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "SQL Day 3 Masterclass Dropping in 1 Hour! (GROUP BY & HAVING) #Shorts",
        "badge": "MASTERCLASS ALERT • 6 PM",
        "hook_text": "SQL Day 3 Masterclass drops in exactly 60 minutes!",
        "code": "-- Dropping at 6:00 PM IST:\n-- 1. Aggregate Functions & NULL Mechanics\n-- 2. Memory Partitioning in GROUP BY\n-- 3. The WHERE vs HAVING Architectural Divide\n-- 4. True 6-Stage SQL Execution Pipeline",
        "caption": "Full 12-Minute SQL Masterclass at 6 PM!",
        "riddle_text": "Day 3 Dropping in 1 Hour! 🔔",
        "speech": (
            "Our SQL Day 3 Masterclass goes live in exactly one hour at 6 PM IST! Today we master the relational aggregation "
            "engine, explain why non-grouped columns cause syntax errors, and explore the internal six-stage SQL execution "
            "pipeline. Subscribe and join us at 6 PM!"
        )
    },
    # 06:00 PM IST -> SQL Masterclass published
    # 07:00 PM IST
    {
        "hour_ist": 19,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "The MongoDB Null Trap: Why { status: null } Matches Missing Fields! #Shorts",
        "badge": "MONGODB SECRETS • DAY 3",
        "hook_text": "Why querying for null returns missing fields in MongoDB",
        "code": "// ❌ Matches status: null AND missing status!\ndb.users.find({ status: null });\n\n// ✅ Matches ONLY explicit null\ndb.users.find({ status: { $exists: true, $type: 'null' } });",
        "caption": "Combine $exists and $type to strictly match explicit nulls!",
        "riddle_text": "Missing Fields vs Explicit Null 🔍",
        "speech": (
            "Did you know that querying for status colon null in MongoDB returns documents where status is null and every "
            "document where the status field is missing altogether? If you want to strictly match explicit null values, "
            "combine dollar-exists true with dollar-type null. Save this tip for your next database audit!"
        )
    },
    # 08:00 PM IST
    {
        "hour_ist": 20,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "How to Find Duplicate Records in SQL in 1 Query #Shorts #SQL",
        "badge": "SQL PATTERNS • DAY 3",
        "hook_text": "How FAANG interviewers test duplicate detection in SQL",
        "code": "-- Identify duplicate email addresses\nSELECT email, COUNT(*)\nFROM users\nGROUP BY email\nHAVING COUNT(*) > 1;",
        "caption": "Group by the key and filter with HAVING COUNT(*) > 1!",
        "riddle_text": "Finding Duplicates in 10M Rows 🚀",
        "speech": (
            "How do you find duplicate email records in a ten-million row database table? Group by the email column and "
            "filter using HAVING COUNT star greater than one! Any record that appears multiple times will be instantly "
            "returned with its duplicate tally. Remember this pattern for your next database interview!"
        )
    },
    # 09:00 PM IST
    {
        "hour_ist": 21,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Bytecode Disassembly: Why List Comprehensions Win #Shorts #Python",
        "badge": "PYTHON INTERNALS • DAY 3",
        "hook_text": "Why list comprehensions run 30% faster at the bytecode level",
        "code": "import dis\n# Imperative loop: Repeated LOAD_METHOD & CALL_METHOD\n# Comprehension: Dedicated C-level LIST_APPEND opcode!\ndis.dis(comp_func)",
        "caption": "Comprehensions use dedicated C opcodes without method lookup overhead!",
        "riddle_text": "Under the Hood with dis.dis() ⚡",
        "speech": (
            "Why do list comprehensions run thirty percent faster than imperative loops? Because CPython compiles them into "
            "dedicated virtual machine instructions featuring the specialized LIST APPEND opcode. This opcode appends items "
            "directly at C-speed, bypassing Python method lookups entirely!"
        )
    },
    # 10:00 PM IST
    {
        "hour_ist": 22,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Guarded Patterns in Java 21: The 'when' Keyword #Shorts #Java",
        "badge": "JAVA 21 • DAY 3",
        "hook_text": "How the 'when' keyword replaces nested if-statements in Java 21",
        "code": "return switch (tx) {\n    case Payment p when p.amount() > 100_000 -> \"HIGH_ALERT\";\n    case Payment p when p.amount() > 0       -> \"APPROVED\";\n    default -> \"REJECTED\";\n};",
        "caption": "Add business rules directly to type pattern matches with 'when'!",
        "riddle_text": "Guarded Patterns in Modern Java 🛡️",
        "speech": (
            "How does the when keyword revolutionize Java control flow? In Java 21, guarded patterns allow you to append "
            "conditional business logic directly to your type patterns. This replaces deeply nested if-statements with flat, "
            "declarative decision matrices that are clean and easy to maintain."
        )
    },
    # 11:00 PM IST
    {
        "hour_ist": 23,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Conditional Aggregations: The SUM(CASE WHEN) Superpower #Shorts #SQL",
        "badge": "SQL PRO TRICK • DAY 3",
        "hook_text": "How senior engineers compute multiple metrics in 1 SQL query",
        "code": "SELECT \n    dept_id,\n    COUNT(*) AS total,\n    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count,\n    SUM(CASE WHEN salary > 100k THEN 1 ELSE 0 END) AS high_earners\nFROM staff GROUP BY dept_id;",
        "caption": "Compute pivot metrics in a single table scan using SUM(CASE WHEN)!",
        "riddle_text": "The 1-Query Pivot Superpower 📊",
        "speech": (
            "How do senior database engineers calculate multiple metrics without running multiple queries? By using "
            "conditional aggregation! Wrapping CASE WHEN statements inside SUM computes custom counts and sums in a single "
            "table scan. It is ten times faster than stitching separate queries together!"
        )
    }
]
'''

with open(CONTENT_DIR / "day3_shorts_data.py", "w", encoding="utf-8") as f:
    f.write(day3_shorts_data)

print("Generated day3_shorts_data.py successfully!")
