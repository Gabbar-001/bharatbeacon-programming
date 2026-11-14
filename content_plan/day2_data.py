# Day 2 Masterclass Data Definitions
from src.tech_animator import COLOR_PYTHON, COLOR_JAVA, COLOR_MONGO, COLOR_SQL

DAY2_MASTERCLASSES = [
    # 1. PYTHON DAY 2
    {
        "track": "python",
        "track_title": "PYTHON MASTERCLASS",
        "episode_info": "DAY 02 OF 60",
        "title": "Python Day 2: Data Structures Under the Hood: Lists, Tuples, Sets & Hash Tables",
        "accent_color": COLOR_PYTHON,
        "playlist_key": "python_longform",
        "tags": ["Python", "Python Data Structures", "Python Tutorial", "Hash Tables", "Time Complexity", "Learn Python", "Python Lists"],
        "slides": [
            {
                "title": "Python's Big 4 Data Structures",
                "bullets": [
                    "Day 2 of our 60-day engineering bootcamp: Mastering data structures.",
                    "Lists: Ordered, mutable, dynamic arrays with O(1) append and O(n) search.",
                    "Tuples: Immutable fixed-size sequences with reduced memory footprint.",
                    "Sets & Dicts: Hash table implementations with O(1) average lookup time."
                ],
                "card_type": "code",
                "filename": "structures.py",
                "code": "# Python's Core 4 Data Structures\nmy_list  = [1, 2, 3]        # Dynamic Array\nmy_tuple = (1, 2, 3)        # Immutable Tuple\nmy_set   = {1, 2, 3}        # Hash Table (Unique)\nmy_dict  = {'id': 1}        # Key-Value Hash Map",
                "speech": (
                    "Welcome to Day 2 of our 60-Day Python Masterclass. Today we dive into the engine room of Python: "
                    "Lists, Tuples, Dictionaries, and Sets. Choosing the wrong data structure can make your code "
                    "a thousand times slower. Today, you will learn the exact memory layout and time complexity "
                    "of each structure so you always choose the optimal one."
                )
            },
            {
                "title": "Memory Layout: Contiguous vs Hash Map",
                "bullets": [
                    "List: Contiguous array of pointers in RAM; over-allocates memory for amortized growth.",
                    "Tuple: Exact memory allocation; frozen at creation time, preventing accidental mutation.",
                    "Set & Dict: Sparse hash table arrays with hash bucket indexes for instant key retrieval."
                ],
                "card_type": "memory",
                "speech": (
                    "Let's look at how Python allocates RAM for each structure. A list is a dynamic array of pointers. "
                    "When you append items, Python secretly over-allocates extra memory slots so future appends take "
                    "constant O of one time. A tuple, by contrast, is allocated to its exact length and never resizes, "
                    "making it lighter on memory and completely thread-safe."
                )
            },
            {
                "title": "The Membership Trap: List vs Set",
                "bullets": [
                    "Searching in a list ('if item in my_list') performs a linear scan: O(n) time.",
                    "Searching in a set ('if item in my_set') computes a hash index: O(1) time.",
                    "On 100,000 items: Set lookup takes 0.0001s, List lookup takes 4.5s!"
                ],
                "card_type": "split",
                "bad_code": "# ❌ ROOKIE TRAP: O(n^2) Linear Scan\nlarge_list = list(range(100_000))\n\ndef check_access(user_ids):\n    for uid in user_ids:\n        if uid in large_list: # O(n) scan!\n            grant()\n# Crawls to a complete halt!",
                "good_code": "# ✅ PRO FIX: O(n) Hash Lookup\nlookup_set = set(range(100_000))\n\ndef check_access(user_ids):\n    for uid in user_ids:\n        if uid in lookup_set: # O(1) instant!\n            grant()\n# Executes in milliseconds!",
                "speech": (
                    "Here is a rookie trap that destroys microservice performance. When you write if user ID in large list, "
                    "Python has to scan every single element one by one from beginning to end. With one hundred thousand "
                    "users, this runs in O of n squared time. If you convert that list to a set, lookups become O of one "
                    "hash lookups, running thousands of times faster."
                )
            },
            {
                "title": "Anti-Pattern: Mutating List During Iteration",
                "bullets": [
                    "Modifying a list (e.g. remove() or pop()) while iterating over it shifts index pointers.",
                    "Python's internal index cursor skips elements silently without throwing an error!",
                    "Always iterate over a copy or use a clean list comprehension filter."
                ],
                "card_type": "code",
                "filename": "mutation_bug.py",
                "code": "# ❌ THE SILENT BUG\nnums = [1, 2, 2, 3, 4]\nfor n in nums:\n    if n == 2:\n        nums.remove(n) # Shifts list in-place!\nprint(nums) # Prints [1, 2, 3, 4]! The second 2 was skipped!\n\n# ✅ THE PRO FIX\nnums = [n for n in nums if n != 2]",
                "speech": (
                    "Look at this subtle bug. We have a list with two number twos, and we iterate over it to remove "
                    "every two. When the first two is deleted, the list shifts left, but the loop counter advances forward. "
                    "The second number two gets skipped silently! Never mutate a list while looping through it. "
                    "Always use a list comprehension instead."
                )
            },
            {
                "title": "FAANG Interview: Hash Collisions in Dicts",
                "bullets": [
                    "Dictionary keys must be hashable (implement __hash__() and __eq__()).",
                    "When two distinct keys produce the same hash value, a Hash Collision occurs.",
                    "Python resolves collisions using Open Addressing with Perturbation probing."
                ],
                "card_type": "code",
                "filename": "hash_collision.py",
                "code": "# Python Key Hashability\nprint(hash('apple'))  # Valid integer hash\n\n# Immutable types are hashable\nvalid_dict = {(1, 2): 'coordinates'}\n\n# Mutable types fail with TypeError\n# invalid_dict = {[1, 2]: 'error'} # TypeError: unhashable type: 'list'",
                "speech": (
                    "Here is a classic FAANG interview question: Why can a tuple be a dictionary key, but a list cannot? "
                    "The answer is Hashability. For Python to place an item into a dictionary bucket in O of one time, "
                    "it must compute a hash value that never changes. Because lists are mutable, their contents can change, "
                    "which would break the hash table. Tuples are immutable, so their hash is guaranteed stable."
                )
            },
            {
                "title": "Day 2 Summary & Homework Challenge",
                "bullets": [
                    "Key Takeaway: Use Sets for membership testing and deduplication.",
                    "Key Takeaway: Never mutate a list while iterating over it.",
                    "Homework Challenge: Drop your solution in the comments: How do you deduplicate a list while preserving original order in 1 line?"
                ],
                "card_type": "code",
                "filename": "homework_day2.py",
                "code": "# DAY 2 HOMEWORK CHALLENGE\n# Given a list with duplicates:\nitems = ['apple', 'banana', 'apple', 'cherry', 'banana']\n\n# How to deduplicate preserving order in 1 line?\n# (Hint: set() loses insertion order!)\n# Drop your answer below!",
                "speech": (
                    "To summarize Day 2: Use Lists when order matters, Tuples for immutable records, Sets for fast lookups, "
                    "and Dictionaries for key-value mappings. Here is your Day 2 homework: How do you remove duplicates from a "
                    "list while preserving the exact original order in just one line of code? Set loses order, so what is the trick? "
                    "Drop your answer in the comments below, hit subscribe, and I will see you tomorrow for Day 3: Control Flow and Iterators."
                )
            }
        ]
    },

    # 2. JAVA DAY 2
    {
        "track": "java",
        "track_title": "JAVA MASTERCLASS",
        "episode_info": "DAY 02 OF 60",
        "title": "Java Day 2: Primitives, Memory Allocation & Type Casting (Stack vs Heap)",
        "accent_color": COLOR_JAVA,
        "playlist_key": "java_longform",
        "tags": ["Java", "Java Primitives", "JVM Memory", "Type Casting", "Learn Java", "Java Tutorial", "Java Overflow"],
        "slides": [
            {
                "title": "The 8 Primitives of Java",
                "bullets": [
                    "Day 2: Understanding primitive types, memory allocations, and casting.",
                    "Numeric Integers: byte (8-bit), short (16-bit), int (32-bit), long (64-bit).",
                    "Floating Points: float (32-bit), double (64-bit).",
                    "Others: boolean (1-bit JVM flag), char (16-bit Unicode character)."
                ],
                "card_type": "code",
                "filename": "Primitives.java",
                "code": "// Java's 8 Primitive Types\nbyte   b = 127;           // -128 to 127\nshort  s = 32_767;        // -32,768 to 32,767\nint    i = 2_147_483_647; // 32-bit standard\nlong   l = 9_223_372_036_854_775_807L;\nfloat  f = 3.14f;\ndouble d = 3.1415926535;\nchar   c = 'A';\nboolean isLive = true;",
                "speech": (
                    "Welcome to Day 2 of our Java Masterclass. Today we examine the eight primitive data types in Java. "
                    "Unlike languages where numbers are generic objects, Java gives you direct control over memory allocation. "
                    "A byte uses eight bits, while a long uses sixty-four bits. Understanding their exact boundaries prevents "
                    "catastrophic overflow bugs in enterprise software."
                )
            },
            {
                "title": "Silent Integer Overflow Disasters",
                "bullets": [
                    "When an integer exceeds its maximum limit, it silently wraps around to negative values!",
                    "Math operations default to 32-bit int before being assigned to a 64-bit long.",
                    "Always append an 'L' suffix to force 64-bit calculation in long math."
                ],
                "card_type": "split",
                "bad_code": "// ❌ SILENT INTEGER OVERFLOW\n// 24 * 60 * 60 * 1000 * 1000\n// Multiplies as 32-bit int first!\nlong microsPerDay = 24 * 60 * 60 * 1000 * 1000;\nSystem.out.println(microsPerDay);\n// Prints: -1855993472 (Negative!)",
                "good_code": "// ✅ PRO FIX: Explicit 64-bit Suffix\n// Append 'L' to force 64-bit math\nlong microsPerDay = 24L * 60 * 60 * 1000 * 1000;\nSystem.out.println(microsPerDay);\n// Prints: 86400000000 (Correct!)",
                "speech": (
                    "Look at this catastrophic bug. If you calculate microseconds in a day without an L suffix, "
                    "Java calculates the product as a thirty-two bit integer before saving it into your long variable. "
                    "The number overflows and wraps around into a negative number! Your timestamps get corrupted. "
                    "Always append an L literal to the first number to force sixty-four bit math."
                )
            },
            {
                "title": "Why Floating Point Fails in Finance",
                "bullets": [
                    "Double and float use IEEE 754 binary fractions; cannot represent decimal 0.1 exactly.",
                    "Performing financial calculations with double leads to rounding drift errors.",
                    "Industry Standard: Always use java.math.BigDecimal for money and transactions."
                ],
                "card_type": "code",
                "filename": "FinanceMath.java",
                "code": "// ❌ FLOATING POINT ROUNDING ERROR\ndouble price = 0.10 + 0.20;\nSystem.out.println(price); // 0.30000000000000004!\n\n// ✅ BANKING GRADE PRECISION\nBigDecimal a = new BigDecimal(\"0.10\");\nBigDecimal b = new BigDecimal(\"0.20\");\nBigDecimal total = a.add(b);\nSystem.out.println(total); // Exactly 0.30!",
                "speech": (
                    "Here is why floating point numbers are strictly banned in banking software. Computers use binary fractions. "
                    "A double cannot represent zero point one exactly, resulting in zero point three followed by a four at the end. "
                    "In accounting, a missing penny across millions of transactions fails regulatory audits. "
                    "Always use BigDecimal with string constructors for financial math."
                )
            },
            {
                "title": "Day 2 Summary & Homework Challenge",
                "bullets": [
                    "Key Takeaway: Primitives live on the Stack; object wrappers live on the Heap.",
                    "Key Takeaway: Beware of silent 32-bit overflow; append L to constants.",
                    "Homework: Why does byte b = 127; b++; System.out.println(b); print -128? Drop your explanation below!"
                ],
                "card_type": "code",
                "filename": "HomeworkDay2.java",
                "code": "// DAY 2 HOMEWORK CHALLENGE\nbyte b = 127;\nb++;\nSystem.out.println(b); // Why does this print -128?\n\n// Drop your explanation in the comments below!",
                "speech": (
                    "To summarize Day 2: Choose primitive types wisely to optimize memory. Use long literals for large "
                    "calculations, and never use double for money. Here is your Day 2 homework: If byte b equals one hundred "
                    "and twenty-seven, why does b plus plus print negative one hundred and twenty-eight? Drop your explanation "
                    "in the comments below! Hit subscribe, and I will see you tomorrow for Day 3: Control Flow and Loops."
                )
            }
        ]
    },

    # 3. MONGODB DAY 2
    {
        "track": "mongodb",
        "track_title": "MONGODB COMPLETE GUIDE",
        "episode_info": "DAY 02 OF 60",
        "title": "MongoDB Day 2: CRUD Mastery: Efficient Queries, Filtering & Projections",
        "accent_color": COLOR_MONGO,
        "playlist_key": "mongodb_longform",
        "tags": ["MongoDB", "NoSQL", "CRUD", "MongoDB Queries", "Projections", "Learn MongoDB", "Database"],
        "slides": [
            {
                "title": "Mastering MongoDB CRUD Operations",
                "bullets": [
                    "Day 2 of our 60-day MongoDB series: Reading, writing, and filtering documents.",
                    "insertOne() vs insertMany(): Atomic batch document insertions.",
                    "find() & findOne(): Querying collections using declarative JSON filters.",
                    "Comparison Operators: $eq, $gt, $gte, $lt, $lte, $in, $ne."
                ],
                "card_type": "code",
                "filename": "crud.js",
                "code": "// MongoDB CRUD Essentials\ndb.orders.insertMany([\n  { user: 'Alice', amount: 120, status: 'PAID' },\n  { user: 'Bob',   amount: 45,  status: 'PENDING' },\n  { user: 'Charlie', amount: 200, status: 'PAID' }\n]);\n\n// Query with comparison filter\ndb.orders.find({ amount: { $gte: 100 }, status: 'PAID' });",
                "speech": (
                    "Welcome to Day 2 of our MongoDB Complete Guide. Today we master CRUD operations: creating, reading, "
                    "updating, and deleting documents. In MongoDB, queries are not written as SQL text strings; they are "
                    "native JSON filter objects. We will learn how to write high-performance query criteria and projection masks."
                )
            },
            {
                "title": "The Power of Field Projections",
                "bullets": [
                    "Projection restricts fields returned from disk, reducing network bandwidth by up to 90%.",
                    "Syntax: { field: 1 } includes, { field: 0 } excludes.",
                    "The '_id' field is returned by default unless explicitly excluded with '{ _id: 0 }'."
                ],
                "card_type": "split",
                "bad_code": "// ❌ ANTI-PATTERN: Full Document Fetch\n// Fetches heavy 2MB document\n// over the wire to UI!\ndb.users.find({\n  city: 'Mumbai'\n});\n// Wastes RAM and network bandwidth!",
                "good_code": "// ✅ PRO FIX: Precise Projection Mask\n// Returns only the 2 required fields\ndb.users.find(\n  { city: 'Mumbai' },\n  { name: 1, email: 1, _id: 0 }\n);\n// 95% faster network transfer!",
                "speech": (
                    "Here is a classic performance mistake in production NoSQL databases. If a user document contains "
                    "order histories, profile images, and activity logs, fetching the entire document wastes megabytes "
                    "of network bandwidth. By adding a projection mask, you tell MongoDB to extract only the name and email, "
                    "cutting network transfer times by ninety-five percent."
                )
            },
            {
                "title": "Day 2 Summary & Homework Challenge",
                "bullets": [
                    "Key Takeaway: Use insertMany for bulk inserts; always use projection masks on find().",
                    "Key Takeaway: Remember that _id is included by default unless suppressed with _id: 0.",
                    "Homework: Write a MongoDB query to find all orders with status 'PAID' and amount > 150 returning only the user and amount. Drop it below!"
                ],
                "card_type": "code",
                "filename": "homework_mongo2.js",
                "code": "// DAY 2 MONGODB CHALLENGE\n// Write a find query for:\n// 1. status == 'PAID'\n// 2. amount > 150\n// 3. Return ONLY user and amount (no _id)\n// Drop your exact mongosh query below!",
                "speech": (
                    "To summarize Day 2: Filter documents efficiently using query operators, and always apply projection "
                    "masks to keep network transfer lean. Here is your Day 2 homework: Write the exact MongoDB shell command "
                    "to find all paid orders over one hundred and fifty dollars, returning only user and amount without the ID. "
                    "Drop your answer in the comments below! Subscribe now, and I will see you tomorrow for Day 3: Updates and Array Filters."
                )
            }
        ]
    },

    # 4. SQL DAY 2
    {
        "track": "sql",
        "track_title": "SQL MASTERCLASS",
        "episode_info": "DAY 02 OF 60",
        "title": "SQL Day 2: The Execution Order: FROM, WHERE, GROUP BY & Index Seeks",
        "accent_color": COLOR_SQL,
        "playlist_key": "sql_longform",
        "tags": ["SQL", "SQL Execution Order", "Database", "SQL Tutorial", "WHERE Clause", "Learn SQL", "PostgreSQL"],
        "slides": [
            {
                "title": "The True SQL Query Execution Order",
                "bullets": [
                    "Day 2 of SQL Mastery: Understanding how the database engine actually processes queries.",
                    "Written Order: SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY.",
                    "Execution Order: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT.",
                    "This is why you CANNOT use a SELECT column alias in the WHERE clause!"
                ],
                "card_type": "code",
                "filename": "execution_order.sql",
                "code": "-- SQL Query Execution Order\n-- 1. FROM & JOIN     (Load data tables)\n-- 2. WHERE           (Filter raw rows)\n-- 3. GROUP BY        (Aggregate into buckets)\n-- 4. HAVING          (Filter aggregated buckets)\n-- 5. SELECT          (Pick & rename columns)\n-- 6. ORDER BY        (Sort output)\n-- 7. LIMIT / OFFSET  (Slice pagination)",
                "speech": (
                    "Welcome to Day 2 of our SQL Masterclass. Ninety percent of developers write SQL based on how the query "
                    "looks on screen. But the database engine does not execute queries from top to bottom. It starts at FROM, "
                    "filters rows in WHERE, aggregates in GROUP BY, and only evaluates the SELECT line near the very end. "
                    "Understanding this order is the secret to debugging query errors."
                )
            },
            {
                "title": "The Wildcard Trap in LIKE Queries",
                "bullets": [
                    "LIKE 'prefix%': Utilizes B-Tree index range scans for fast O(log n) lookups.",
                    "LIKE '%substring%': Cannot use B-Tree indexes! Forces a catastrophic full table scan.",
                    "On a table with 10M rows: Prefix search takes 3ms, leading wildcard search takes 14 seconds!"
                ],
                "card_type": "split",
                "bad_code": "-- ❌ LEADING WILDCARD (Full Table Scan)\n-- Cannot use B-Tree index on email!\n-- Scans all 10M rows from disk!\nSELECT * FROM customers\nWHERE email LIKE '%@gmail.com';\n-- Query Time: 12.4s (High CPU Load!)",
                "good_code": "-- ✅ PRO FIX: Sargsable Index Seek\n-- Uses B-Tree index seek on username!\nSELECT * FROM customers\nWHERE username LIKE 'alex%';\n-- Query Time: 2ms (Lightning Fast!)",
                "speech": (
                    "Here is a common database killer in production. When you put a wildcard percentage sign at the "
                    "beginning of a LIKE query, the database engine cannot use its B-Tree index. It has to load every single row "
                    "from disk into memory and inspect the characters. On a ten-million row database, this spikes CPU to "
                    "one hundred percent. Always use prefix seeks or full-text search indexes."
                )
            },
            {
                "title": "Day 2 Summary & Homework Challenge",
                "bullets": [
                    "Key Takeaway: SQL executes FROM and WHERE before SELECT.",
                    "Key Takeaway: Leading wildcards disable B-Tree indexes; use prefix seeks.",
                    "Homework: Why does SELECT * FROM users WHERE salary = NULL return 0 rows even when salaries are NULL? Drop your answer below!"
                ],
                "card_type": "code",
                "filename": "homework_sql2.sql",
                "code": "-- DAY 2 SQL HOMEWORK CHALLENGE\n-- Why does this query return 0 rows,\n-- even when there are records with NULL salary?\nSELECT * FROM employees WHERE salary = NULL;\n\n-- What is the correct syntax?\n-- Drop your explanation in the comments below!",
                "speech": (
                    "To summarize Day 2: Always remember the true SQL execution order. Avoid leading wildcards in LIKE queries "
                    "to keep your indexes active. Here is your Day 2 homework: Why does WHERE salary equals NULL return zero "
                    "rows even when there are NULL values in the table? What is the correct SQL keyword to use? "
                    "Drop your answer below! Subscribe now, and I will see you tomorrow for Day 3: JOINS and Relationships."
                )
            }
        ]
    }
]
