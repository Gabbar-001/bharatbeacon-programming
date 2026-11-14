# Day 2 - 20 Viral Tech Shorts (1 Short per Hour)

DAY2_SHORTS = [
    # 00:00 AM IST (Midnight Launch)
    {
        "hour_ist": 0,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Why List vs Set in Python Makes Your Code 1000x Slower #Shorts #Python",
        "badge": "PYTHON PERFORMANCE • DAY 2",
        "hook_text": "Why checking 'if x in list' makes your Python code 1000x slower",
        "code": "# 100,000 items\nif x in my_list: # O(n) scan -> 4.5s!\n\nif x in my_set:  # O(1) hash -> 0.0001s!",
        "caption": "Always use Set for membership lookups!",
        "riddle_text": "O(n) Linear vs O(1) Hash ⚡",
        "speech": (
            "Why does if x in list make your Python code a thousand times slower? Because searching a list requires "
            "scanning every single item one by one. A set computes a hash code and finds the element in constant O of one "
            "time. Convert your lookup lists to sets! Full Day 2 Masterclass drops at 10 AM."
        )
    },
    # 01:00 AM IST
    {
        "hour_ist": 1,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The Silent Integer Overflow Disaster in Java #Shorts #Java",
        "badge": "JAVA BUG HUNT • DAY 2",
        "hook_text": "The silent integer overflow bug that took down bank servers",
        "code": "// 24 * 60 * 60 * 1000 * 1000\n// Multiplies as 32-bit int first!\nlong micros = 24 * 60 * 60 * 1000 * 1000;\n\n// Output: -1855993472 😱",
        "caption": "Append 'L' to force 64-bit calculation!",
        "riddle_text": "Why is it negative? Overflow! 💥",
        "speech": (
            "Look at this silent Java bug that took down banking servers. When you multiply constants into a long variable, "
            "Java computes them as thirty-two bit integers first. The calculation overflows into a negative number! "
            "Always append an L suffix to the first number. Day 2 Masterclass link in comments!"
        )
    },
    # 02:00 AM IST
    {
        "hour_ist": 2,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "The 90% Bandwidth Hack in MongoDB: Field Projections #Shorts #MongoDB",
        "badge": "MONGODB SECRETS • DAY 2",
        "hook_text": "How one projection mask saves 90% of MongoDB network bandwidth",
        "code": "// ❌ Heavy 2MB document\ndb.users.find({ city: 'BLR' });\n\n// ✅ 95% Faster Mask\ndb.users.find({ city: 'BLR' }, { name: 1, email: 1, _id: 0 });",
        "caption": "Never fetch full docs when you need 2 fields!",
        "riddle_text": "Masking Saves Gigabytes of RAM 🚀",
        "speech": (
            "How does one simple projection mask save ninety percent of MongoDB network bandwidth? When documents "
            "have nested profiles and transaction histories, fetching the entire document chokes the network. "
            "Use projection masks to return only the fields your UI needs. Learn MongoDB CRUD at 2 PM today!"
        )
    },
    # 03:00 AM IST
    {
        "hour_ist": 3,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Why You CANNOT Use a Column Alias in a WHERE Clause #Shorts #SQL",
        "badge": "SQL INTERNALS • DAY 2",
        "hook_text": "Why SQL throws an error when you use an alias in a WHERE clause",
        "code": "-- ❌ FAILS with Unknown Column 'bonus'\nSELECT salary * 0.2 AS bonus\nFROM employees\nWHERE bonus > 5000;\n\n-- Because WHERE runs BEFORE SELECT!",
        "caption": "SQL Execution Order: FROM -> WHERE -> SELECT",
        "riddle_text": "Execution Order is NOT Written Order! 🧠",
        "speech": (
            "Why does SQL throw an unknown column error when you filter by a column alias in a WHERE clause? "
            "Because SQL does not run from top to bottom. The database engine executes the WHERE filter before "
            "it ever looks at the SELECT clause! Learn the true SQL execution order in our 6 PM masterclass."
        )
    },
    # 04:00 AM IST
    {
        "hour_ist": 4,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "The Silent Bug: Modifying a List While Looping in Python #Shorts #Python",
        "badge": "PYTHON GOTCHAS • DAY 2",
        "hook_text": "The silent bug that skips elements when mutating Python lists",
        "code": "nums = [1, 2, 2, 3, 4]\nfor n in nums:\n    if n == 2:\n        nums.remove(n)\n\nprint(nums) # [1, 2, 3, 4]! 2 skipped!",
        "caption": "Use list comprehensions instead of in-place mutation!",
        "riddle_text": "Index shifts skip duplicate items! 😱",
        "speech": (
            "Look at this sneaky Python bug. When we remove a two from a list while iterating, the remaining items "
            "shift left, but the internal loop counter advances forward. The second number two gets skipped silently! "
            "Never remove items from a list while looping over it. Use a list comprehension instead."
        )
    },
    # 05:00 AM IST
    {
        "hour_ist": 5,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Why Floating Point Math is BANNED in Banking Code #Shorts #Java",
        "badge": "JAVA ENTERPRISE • DAY 2",
        "hook_text": "Why double and float are strictly forbidden in banking software",
        "code": "// Floating point rounding error\ndouble sum = 0.10 + 0.20;\nSystem.out.println(sum);\n// Output: 0.30000000000000004!\n\n// Solution: BigDecimal(\"0.10\")",
        "caption": "Always use BigDecimal for financial precision!",
        "riddle_text": "Missing pennies fail regulatory audits 💰",
        "speech": (
            "Why are float and double strictly forbidden in banking code? Because computers use binary fractions. "
            "Adding zero point one and zero point two gives zero point three followed by a four at the end! "
            "Across millions of transactions, rounding drift creates missing pennies. Always use BigDecimal."
        )
    },
    # 06:00 AM IST
    {
        "hour_ist": 6,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "Querying Nested Arrays Like a Senior MongoDB Engineer #Shorts #MongoDB",
        "badge": "MONGODB TRICKS • DAY 2",
        "hook_text": "How senior engineers query nested documents using dot notation",
        "code": "// Document with nested profile\n{\n  name: 'Sam',\n  address: { city: 'Mumbai', pin: 400001 }\n}\n\n// Query directly into child object:\ndb.users.find({ 'address.city': 'Mumbai' });",
        "caption": "Dot notation accesses nested fields seamlessly!",
        "riddle_text": "Nested Queries Without Slow SQL Joins ⚡",
        "speech": (
            "How do senior engineers query nested documents in MongoDB? With dot notation! You can query directly "
            "into child objects by wrapping the path in quotes, like address dot city equals Mumbai. "
            "No relational joins needed. Check out our MongoDB Masterclass at two PM today!"
        )
    },
    # 07:00 AM IST
    {
        "hour_ist": 7,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Why LIKE '%text%' Destroys Database Performance #Shorts #SQL",
        "badge": "SQL PERFORMANCE • DAY 2",
        "hook_text": "Why putting % at the start of a LIKE query kills your database",
        "code": "-- ❌ Leading wildcard: FULL TABLE SCAN!\nSELECT * FROM users WHERE email LIKE '%@gmail.com';\n-- 10M rows = 14 seconds!\n\n-- ✅ Prefix seek: INDEX SCAN!\nSELECT * FROM users WHERE username LIKE 'alex%';",
        "caption": "Leading % disables B-Tree index seeks!",
        "riddle_text": "From 14 seconds down to 2 milliseconds! ⚡",
        "speech": (
            "Why does putting a percentage sign at the start of a LIKE query destroy database performance? "
            "Because B-Tree indexes sort from left to right. A leading wildcard makes the index useless, "
            "forcing the database to scan every single row on disk! Use prefix seeks or full-text indexes."
        )
    },
    # 08:00 AM IST
    {
        "hour_ist": 8,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Deduplicate a Python List in 1 Line (Preserving Order) #Shorts #Python",
        "badge": "PYTHON ONE-LINERS • DAY 2",
        "hook_text": "How to deduplicate a Python list in one line while preserving order",
        "code": "items = ['apple', 'banana', 'apple', 'cherry']\n\n# set(items) loses original order!\n# Pro trick (Python 3.7+):\ndupes_removed = list(dict.fromkeys(items))\n\nprint(dupes_removed)",
        "caption": "list(dict.fromkeys()) preserves insertion order!",
        "riddle_text": "['apple', 'banana', 'cherry'] ✅",
        "speech": (
            "How do you remove duplicates from a Python list while preserving the exact original order? "
            "If you use set, you scramble the order. The pro trick in Python is list of dict dot fromkeys. "
            "Since Python dictionaries maintain insertion order, duplicates are removed in O of n time!"
        )
    },
    # 09:00 AM IST
    {
        "hour_ist": 9,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Python Day 2 Masterclass Dropping in 1 Hour! (Data Structures) #Shorts #Python",
        "badge": "PREMIERE ALERT • DAY 2",
        "hook_text": "Python Day 2 Masterclass drops at 10 AM IST today!",
        "code": "# Topics dropping in 60 mins:\n- Lists vs Tuples memory benchmark\n- Sets vs Hash Tables under the hood\n- O(1) vs O(n) algorithmic speed\n- FAANG Interview Hash Challenges",
        "caption": "Premiere at 10:00 AM IST on BharatBeacon!",
        "riddle_text": "Get ready for Day 2! 🚀",
        "speech": (
            "Premiere alert! Day 2 of our 60-Day Python Masterclass drops in one hour at ten AM IST. "
            "We are going deep into data structures, memory layouts, and time complexities. "
            "Set your reminder and subscribe to BharatBeacon!"
        )
    },
    # 11:00 AM IST
    {
        "hour_ist": 11,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Java Day 2 Masterclass Dropping in 1 Hour! (Primitives & Casting) #Shorts #Java",
        "badge": "PREMIERE ALERT • DAY 2",
        "hook_text": "Java Day 2 Masterclass drops at 12 PM IST today!",
        "code": "// Topics dropping at 12:00 PM:\n- 8 Primitives & Stack memory frames\n- Silent integer overflow traps\n- Why float is banned in banking\n- Autoboxing performance benchmarks",
        "caption": "Premiere at 12:00 PM IST on BharatBeacon!",
        "riddle_text": "JVM Masterclass in 60 mins! ☕",
        "speech": (
            "Java engineers, get ready! Day 2 of our Java Masterclass drops in one hour at twelve PM IST. "
            "We are breaking down primitive types, memory frames, and numeric overflow traps. "
            "Subscribe now so you never miss an episode!"
        )
    },
    # 13:00 PM IST
    {
        "hour_ist": 13,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "MongoDB Day 2 Masterclass Dropping in 1 Hour! (CRUD Mastery) #Shorts #MongoDB",
        "badge": "PREMIERE ALERT • DAY 2",
        "hook_text": "MongoDB Day 2 Masterclass drops at 2 PM IST today!",
        "code": "// Topics dropping at 2:00 PM:\n- insertMany vs insertOne atomicity\n- Declarative JSON query filters\n- Saving 90% bandwidth with projections\n- Dot notation on nested documents",
        "caption": "Premiere at 02:00 PM IST on BharatBeacon!",
        "riddle_text": "NoSQL Mastery in 60 mins! 🍃",
        "speech": (
            "Premiere alert! Day 2 of our MongoDB Complete Guide drops in one hour at two PM IST. "
            "We master CRUD operations, comparison operators, and projection masks to supercharge your apps. "
            "Subscribe to BharatBeacon!"
        )
    },
    # 15:00 PM IST
    {
        "hour_ist": 15,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Why Python Dict Keys MUST Be Immutable #Shorts #Python",
        "badge": "PYTHON INTERVIEW • DAY 2",
        "hook_text": "Why can tuples be dictionary keys, but lists throw an error?",
        "code": "# Valid\nd = {(1, 2): 'coordinates'} # Tuple is immutable\n\n# Invalid\n# d = {[1, 2]: 'error'} # TypeError: unhashable type: 'list'",
        "caption": "Dictionary keys must implement __hash__() and __eq__()!",
        "riddle_text": "Mutable objects cannot be hashed! 🧠",
        "speech": (
            "Why can a tuple be a dictionary key in Python, but a list throws a TypeError? "
            "Because dictionary lookups require a permanent hash code. If a list could be a key and you modified it, "
            "its hash would change, and Python could never find your key again! Keys must be immutable."
        )
    },
    # 16:00 PM IST
    {
        "hour_ist": 16,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Java Byte Overflow Riddle: What Happens at 127 + 1? #Shorts #Java",
        "badge": "JAVA PUZZLE • DAY 2",
        "hook_text": "What happens when you increment a byte past 127 in Java?",
        "code": "byte b = 127;\nb++;\n\nSystem.out.println(b);\n// What does this print?\n// A) 128   B) -128   C) Compile Error",
        "caption": "Two's complement wraps 127 to -128!",
        "riddle_text": "Answer: B) -128! 💥",
        "speech": (
            "Here is a classic Java interview riddle. If byte b equals one hundred and twenty-seven, what does "
            "b plus plus print? Is it one hundred and twenty-eight, negative one hundred and twenty-eight, "
            "or an error? The answer is negative one hundred and twenty-eight! In two's complement binary, "
            "flipping the highest bit wraps around to the lowest negative value."
        )
    },
    # 17:00 PM IST
    {
        "hour_ist": 17,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "SQL Day 2 Masterclass Dropping in 1 Hour! (Query Execution) #Shorts #SQL",
        "badge": "PREMIERE ALERT • DAY 2",
        "hook_text": "SQL Day 2 Masterclass drops at 6 PM IST today!",
        "code": "-- Topics dropping at 6:00 PM:\n- True query execution order\n- Why WHERE runs before SELECT\n- Wildcard index traps in LIKE\n- Sargsable query optimization",
        "caption": "Premiere at 06:00 PM IST on BharatBeacon!",
        "riddle_text": "Database Engineering in 60 mins! 🗄️",
        "speech": (
            "Database engineers, get ready! Day 2 of our SQL Masterclass drops in one hour at six PM IST. "
            "We are pulling back the curtain on how the database engine executes queries under the hood. "
            "Subscribe to BharatBeacon!"
        )
    },
    # 19:00 PM IST
    {
        "hour_ist": 19,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "Why Does MongoDB Return _id by Default? #Shorts #MongoDB",
        "badge": "MONGODB QUIRKS • DAY 2",
        "hook_text": "Why does MongoDB return _id even when you didn't ask for it?",
        "code": "// Query asking for only 'name'\ndb.users.find({}, { name: 1 });\n// Output: { _id: ObjectId(...), name: 'Alex' }\n\n// Pro fix: Explicitly suppress _id\ndb.users.find({}, { name: 1, _id: 0 });",
        "caption": "Always use _id: 0 if you don't need the primary key!",
        "riddle_text": "_id is the only field included by default! ⚡",
        "speech": (
            "Why does MongoDB always return the underscore ID field even when you explicitly asked for just the name? "
            "Because MongoDB guarantees every document has a primary key. The ID is the only field included by default "
            "in projections. To remove it, you must explicitly write underscore ID colon zero."
        )
    },
    # 20:00 PM IST
    {
        "hour_ist": 20,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Why 'WHERE column = NULL' NEVER Works in SQL #Shorts #SQL",
        "badge": "SQL GOTCHAS • DAY 2",
        "hook_text": "Why WHERE salary = NULL returns 0 rows even when records exist",
        "code": "-- ❌ ALWAYS RETURNS 0 ROWS!\nSELECT * FROM employees WHERE salary = NULL;\n-- NULL = NULL evaluates to UNKNOWN!\n\n-- ✅ PRO SYNTAX\nSELECT * FROM employees WHERE salary IS NULL;",
        "caption": "Use 'IS NULL' instead of '= NULL' in SQL!",
        "riddle_text": "SQL uses Three-Valued Logic! 🧠",
        "speech": (
            "Why does WHERE salary equals NULL return zero rows in SQL even when you have null records? "
            "Because SQL uses Three-Valued Logic: True, False, and Unknown. Comparing anything to NULL, "
            "even NULL equals NULL, evaluates to Unknown! You must always use the IS NULL operator."
        )
    },
    # 21:00 PM IST
    {
        "hour_ist": 21,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "List vs Tuple: The Memory Difference You Never Knew #Shorts #Python",
        "badge": "PYTHON MEMORY • DAY 2",
        "hook_text": "The hidden memory overhead of Python Lists compared to Tuples",
        "code": "import sys\n\nt = (1, 2, 3, 4, 5)\nl = [1, 2, 3, 4, 5]\n\nprint(sys.getsizeof(t)) # 80 bytes (Exact)\nprint(sys.getsizeof(l)) # 120 bytes (Over-allocated!)",
        "caption": "Tuples use 33% less memory and are completely immutable!",
        "riddle_text": "Lists over-allocate slots for amortized O(1) appends 📦",
        "speech": (
            "Look at the hidden memory difference between a Python List and a Tuple. Even with the exact same numbers, "
            "the list consumes thirty-three percent more RAM than the tuple. Python lists secretly over-allocate "
            "extra memory slots to support fast appends. Use tuples for static configuration data!"
        )
    },
    # 22:00 PM IST
    {
        "hour_ist": 22,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The Autoboxing Trap That Slows Java Code 10x #Shorts #Java",
        "badge": "JAVA PERFORMANCE • DAY 2",
        "hook_text": "The sneaky autoboxing trap that makes Java code 10x slower",
        "code": "// ❌ ROOKIE: Long wrapper object in loop\nLong sum = 0L; // Object wrapper!\nfor (long i = 0; i < 1_000_000; i++) {\n    sum += i;  // Creates 1M Long objects on Heap!\n}\n\n// ✅ PRO: primitive long sum = 0L; (10x faster!)",
        "caption": "Never use wrapper objects (Integer, Long) in hot loops!",
        "riddle_text": "1,000,000 garbage objects created on Heap! 💥",
        "speech": (
            "Here is a sneaky performance killer in Java. If you declare your accumulator variable as an uppercase Long "
            "object instead of a primitive long, Java creates one million temporary wrapper objects on the Heap during the loop! "
            "This triggers garbage collection lag and slows execution by ten times. Always use primitives in loops."
        )
    },
    # 23:00 PM IST
    {
        "hour_ist": 23,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "The Operator Precedence Trap with AND & OR in SQL #Shorts #SQL",
        "badge": "SQL TRAPS • DAY 2",
        "hook_text": "The operator precedence trap that leaks sensitive data in SQL",
        "code": "-- ❌ TRAP: AND has higher precedence than OR!\nSELECT * FROM accounts\nWHERE is_active = 1 AND balance > 1000 OR is_admin = 1;\n-- Admin accounts leak regardless of active status!\n\n-- ✅ PRO FIX: Always wrap with parentheses\nWHERE is_active = 1 AND (balance > 1000 OR is_admin = 1);",
        "caption": "Always use parentheses when combining AND with OR!",
        "riddle_text": "Operator Precedence Can Leak Sensitive Data 🛡️",
        "speech": (
            "Here is a dangerous SQL trap that can leak sensitive data in production. In SQL, AND has higher precedence "
            "than OR. Without parentheses, your query might return all admin accounts even if they were deactivated! "
            "Always wrap your OR conditions in parentheses to protect business logic. Day 3 drops tomorrow at 6 PM!"
        )
    }
]
