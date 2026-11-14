# Day 1 - 24 Viral Shorts Data (1 Short per Hour)

DAY1_SHORTS = [
    # 00:00 AM IST (Midnight Launch)
    {
        "hour_ist": 0,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Why a = b in Python Breaks Your Code at 2 AM #Shorts #Python",
        "badge": "PYTHON TRICK #1 • DAY 1",
        "hook_text": "Why a = b in Python will break your production code at 2 AM",
        "code": "a = [1, 2, 3]\nb = a  # Pointer copied!\nb.append(99)\n\nprint(a)",
        "caption": "Never assign lists without .copy()!",
        "riddle_text": "Output: [1, 2, 3, 99] 😱",
        "speech": (
            "Why does a equals b in Python break your code at two AM? Look at this code snippet. "
            "You think you made a copy, but when you append to b, a changes too! "
            "Both variables point to the exact same memory address. Never assign lists without dot copy. "
            "Full Day 1 Masterclass link in the comments below!"
        )
    },
    # 01:00 AM IST
    {
        "hour_ist": 1,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Why Banks Still Pay $200k for Java After 30 Years #Shorts #Java",
        "badge": "JAVA INTERNALS • DAY 1",
        "hook_text": "Why the world's biggest banks still run on Java after 30 years",
        "code": "// Java Bytecode Verification\n// Strict memory isolation\n// Zero direct pointer corruption\npublic class BankSecurity {}",
        "caption": "The JVM Memory Fortress in 40s",
        "riddle_text": "Write Once, Run Anywhere 🛡️",
        "speech": (
            "Why do global banks still run on Java after thirty years? It is not the syntax; it is the Java "
            "Virtual Machine. Java completely blocks developers from directly manipulating raw memory pointers, "
            "preventing buffer overflow attacks that plague other languages. Check out our Java Masterclass at twelve PM!"
        )
    },
    # 02:00 AM IST
    {
        "hour_ist": 2,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "Why Amazon Tore Down SQL Tables for NoSQL Documents #Shorts #MongoDB",
        "badge": "MONGODB SECRETS • DAY 1",
        "hook_text": "Why Amazon and Uber tore down SQL tables for NoSQL documents",
        "code": "// One unified JSON document\n{\n  rider: 'Alex',\n  trip: { from: 'BLR', to: 'Airport' },\n  payment: { status: 'PAID' }\n}",
        "caption": "No More 5-Table Slow JOINs!",
        "riddle_text": "Read Together = Store Together ⚡",
        "speech": (
            "Why did Amazon and Uber move core microservices to MongoDB? Because real-world data is nested and dynamic. "
            "Instead of splitting a customer order into five normalized tables and doing slow joins, MongoDB stores "
            "it as one unified document. Learn NoSQL schema design in our MongoDB masterclass at two PM!"
        )
    },
    # 03:00 AM IST
    {
        "hour_ist": 3,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "What Happens When a Bank DB Crashes Mid-Transfer? #Shorts #SQL",
        "badge": "SQL ACID SECRETS • DAY 1",
        "hook_text": "What happens when a database crashes during a $10,000 transfer?",
        "code": "BEGIN TRANSACTION;\nUPDATE accts SET bal = bal - 10000;\n-- CRASH HERE!\n-- Automatic ROLLBACK triggers!\nCOMMIT;",
        "caption": "ACID Atomicity in 30 Seconds",
        "riddle_text": "All or Nothing Execution 🔒",
        "speech": (
            "What happens if power cuts halfway through a ten thousand dollar wire transfer? Without ACID transactions, "
            "your money disappears. Relational databases enforce Atomicity: either both the debit and credit succeed, "
            "or the transaction rolls back as if it never happened. Master SQL engineering at six PM today!"
        )
    },
    # 04:00 AM IST
    {
        "hour_ist": 4,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Python Small Integer Caching Mystery (256 vs 257) #Shorts #Python",
        "badge": "PYTHON RIDDLE • DAY 1",
        "hook_text": "Why is 256 is 256 True, but 257 is 257 False in Python?",
        "code": "x = 256; y = 256\nprint(x is y)  # True!\n\na = 257; b = 257\nprint(a is b)  # False!",
        "caption": "Python Pre-allocates -5 to 256!",
        "riddle_text": "Guess Why: Memory Cache 🧠",
        "speech": (
            "Can you solve this Python riddle? x equals 256, y equals 256. x is y is True! But when you do the same "
            "with 257, Python says False! Why? Because Python pre-allocates small integers from negative five to "
            "256 in memory at startup. Subscribe for daily Python interview questions!"
        )
    },
    # 05:00 AM IST
    {
        "hour_ist": 5,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The String Pool Trap in Java (== vs .equals) #Shorts #Java",
        "badge": "JAVA INTERVIEW • DAY 1",
        "hook_text": "Why s1 == s2 is True, but s1 == new String() is False in Java",
        "code": "String s1 = \"Java\";\nString s2 = \"Java\";\nString s3 = new String(\"Java\");\n\nprint(s1 == s2); // true\nprint(s1 == s3); // false!",
        "caption": "String Constant Pool Explained",
        "riddle_text": "Never use 'new String()' 🚫",
        "speech": (
            "Never create Strings with the new keyword in Java. When you use string literals, Java stores them in the "
            "String Constant Pool to save memory. When you use new String, you bypass the pool and create redundant "
            "heap allocations. Always compare Strings with dot equals, not double equals!"
        )
    },
    # 06:00 AM IST
    {
        "hour_ist": 6,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "What is Secretly Hidden Inside a MongoDB ObjectId? #Shorts #MongoDB",
        "badge": "MONGODB TRICK • DAY 1",
        "hook_text": "What is secretly hidden inside a 12-byte MongoDB ObjectId?",
        "code": "ObjectId('672f09a12c8b74e89f10a123')\n\n// 4 Bytes: Unix Timestamp\n// 5 Bytes: Machine/Process ID\n// 3 Bytes: Increment Counter",
        "caption": "Extract Date Without a Timestamp Column!",
        "riddle_text": "id.getTimestamp() 📅",
        "speech": (
            "Did you know MongoDB ObjectIds are not random numbers? The first four bytes contain the exact Unix "
            "timestamp the document was created. That means every document in MongoDB is automatically sortable "
            "by date without needing a created at column! Check out our full MongoDB masterclass today at two PM!"
        )
    },
    # 07:00 AM IST
    {
        "hour_ist": 7,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "Primary Key vs Unique Key: The Crucial Difference #Shorts #SQL",
        "badge": "SQL INTERVIEW • DAY 1",
        "hook_text": "Primary Key vs Unique Key: Can a Unique Key contain NULL?",
        "code": "-- Primary Key: 1 per table, NO NULLs\n-- Unique Key: Multiple allowed, CAN have NULL!\n\nCREATE TABLE users (\n    id INT PRIMARY KEY,\n    email VARCHAR(100) UNIQUE\n);",
        "caption": "Yes! Unique Keys Allow NULL Values",
        "riddle_text": "Save This For Your Next Interview 💡",
        "speech": (
            "Here is a top SQL interview question: Can a Unique Key contain NULL values? Yes! While a Primary Key "
            "forbids NULLs completely and you can only have one per table, a table can have multiple Unique constraints, "
            "and in most SQL databases, Unique columns permit NULLs. Follow for daily SQL engineering tips!"
        )
    },
    # 08:00 AM IST
    {
        "hour_ist": 8,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Python 1-Line Swap Magic: a, b = b, a #Shorts #Python",
        "badge": "PYTHON CLEAN CODE • DAY 1",
        "hook_text": "How Python swaps two numbers in 1 line without a temp variable",
        "code": "a = 10\nb = 20\n\n# The 1-Line Swap\na, b = b, a\n\nprint(a, b) # 20, 10!",
        "caption": "Tuple Packing & Unpacking Under the Hood",
        "riddle_text": "Clean Idiomatic Python ⚡",
        "speech": (
            "In other languages, swapping two variables requires a temporary variable. In Python, you can write "
            "a comma b equals b comma a. Under the hood, Python packs b and a into a tuple on the stack and unpacks "
            "them simultaneously into the variables. Clean, fast, and idiomatic. Masterclass drops at ten AM!"
        )
    },
    # 09:00 AM IST
    {
        "hour_ist": 9,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Python Day 1 Masterclass Dropping in 1 Hour! #Shorts #Python",
        "badge": "MASTERCLASS TEASER • DAY 1",
        "hook_text": "Day 1 of our 60-Day Python Masterclass drops at 10:00 AM IST!",
        "code": "def master_python_in_60_days():\n    topics = ['Memory', 'OOP', 'FastAPI']\n    return 'Zero to Production Engineer'\n\n# Day 1 drops in 1 hour!",
        "caption": "Python Day 1: Memory & Pointers",
        "riddle_text": "Starts at 10:00 AM IST 🔔",
        "speech": (
            "Attention developers! Day 1 of our 60-Day Python Masterclass drops in one hour at ten AM IST. "
            "We are breaking down how Python actually manages memory, Stack versus Heap, and how to avoid the "
            "rookie mutable defaults trap. Subscribe now so you do not miss the premiere!"
        )
    },
    # 10:00 AM IST (Long-form Python masterclass publishes now!)
    # 11:00 AM IST
    {
        "hour_ist": 11,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Java Day 1 Masterclass Dropping in 1 Hour! #Shorts #Java",
        "badge": "MASTERCLASS TEASER • DAY 1",
        "hook_text": "Day 1 of our 60-Day Java Masterclass drops at 12:00 PM IST!",
        "code": "public class JavaDay1 {\n    // Inside the JVM\n    // Bytecode, ClassLoader & Memory\n    // Premieres at 12:00 PM IST!\n}",
        "caption": "Inside the JVM Architecture",
        "riddle_text": "Starts at 12:00 PM IST ☕",
        "speech": (
            "Day 1 of our 60-Day Java Masterclass goes live in one hour at twelve PM IST. We are stepping inside "
            "the Java Virtual Machine, dissecting bytecode, and mastering the String Constant Pool. Check out the "
            "Java playlist on our channel!"
        )
    },
    # 12:00 PM IST (Long-form Java masterclass publishes now!)
    # 01:00 PM IST
    {
        "hour_ist": 13,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "MongoDB Day 1 Masterclass Dropping in 1 Hour! #Shorts #MongoDB",
        "badge": "MASTERCLASS TEASER • DAY 1",
        "hook_text": "Day 1 of our 60-Day MongoDB Masterclass drops at 2:00 PM IST!",
        "code": "// MongoDB 60-Day Complete Guide\n// Documents, Collections & BSON\n// Premieres at 2:00 PM IST!",
        "caption": "Beyond Rows & Tables in NoSQL",
        "riddle_text": "Starts at 2:00 PM IST 🍃",
        "speech": (
            "Day 1 of our 60-Day MongoDB Masterclass drops in one hour at two PM IST. Learn how modern microservices "
            "store dynamic nested documents and why BSON delivers sub-millisecond query speed. Subscribe now!"
        )
    },
    # 02:00 PM IST (Long-form MongoDB masterclass publishes now!)
    # 03:00 PM IST
    {
        "hour_ist": 15,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "Spot the Bug: The Mutable Default List Trap #Shorts #Python",
        "badge": "SPOT THE BUG • DAY 1",
        "hook_text": "Can you spot the security bug in this Python registration code?",
        "code": "def register(user, perms=[]):\n    perms.append('read')\n    return perms\n\nadmin = register('admin')\nguest = register('guest')",
        "caption": "Default Args Evaluate ONCE at Load Time!",
        "riddle_text": "guest gets ['read', 'read'] 🚨",
        "speech": (
            "Can you spot the critical bug in this function? When guest calls register, they get two read permissions! "
            "In Python, default arguments evaluate only once when the file loads, so all callers share the same list. "
            "Always use None and initialize inside. Full breakdown in our Day 1 lecture!"
        )
    },
    # 04:00 PM IST
    {
        "hour_ist": 16,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "The String Concatenation Loop Trap in Java #Shorts #Java",
        "badge": "JAVA PERFORMANCE • DAY 1",
        "hook_text": "Why s += 'data' in a loop freezes your Java application",
        "code": "// ❌ 10,000 Garbage Objects on Heap\nString s = \"\";\nfor(int i=0; i<10000; i++) s += i;\n\n// ✅ 1 Mutable Buffer\nStringBuilder sb = new StringBuilder();",
        "caption": "Always Use StringBuilder in Loops!",
        "riddle_text": "Eliminate GC Freezes 🚀",
        "speech": (
            "Never concatenate strings using plus equals inside a loop in Java. Because Strings are immutable, every "
            "iteration creates a brand-new object on the Heap. In ten thousand iterations, you create ten thousand garbage "
            "objects, freezing your server during Garbage Collection. Always use StringBuilder!"
        )
    },
    # 05:00 PM IST
    {
        "hour_ist": 17,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "SQL Day 1 Masterclass Dropping in 1 Hour! #Shorts #SQL",
        "badge": "MASTERCLASS TEASER • DAY 1",
        "hook_text": "Day 1 of our 60-Day SQL Masterclass drops at 6:00 PM IST!",
        "code": "-- SQL 60-Day Zero to Hero\n-- ACID Transactions & Relational Schemas\n-- Premieres at 6:00 PM IST!",
        "caption": "ACID Properties & Constraints",
        "riddle_text": "Starts at 6:00 PM IST 🗄️",
        "speech": (
            "Day 1 of our 60-Day SQL Masterclass goes live in one hour at six PM IST. We are breaking down ACID transactions, "
            "table constraints, and the orphaned row disaster. Hit subscribe and join us for the premiere!"
        )
    },
    # 06:00 PM IST (Long-form SQL masterclass publishes now!)
    # 07:00 PM IST
    {
        "hour_ist": 19,
        "track": "mongodb",
        "playlist_key": "mongodb_shorts",
        "title": "The 16MB MongoDB Document Limit Trap #Shorts #MongoDB",
        "badge": "MONGODB GOTCHA • DAY 1",
        "hook_text": "The 16 Megabyte constraint that crashes viral MongoDB apps",
        "code": "// ❌ Unbounded Array Danger\n{\n  title: 'Viral Video',\n  comments: [ ... 100,000 items ... ]\n  // Hits 16MB ceiling and CRASHES!\n}",
        "caption": "Never Store Infinite Arrays in 1 Doc!",
        "riddle_text": "Use Parent Referencing 🛡️",
        "speech": (
            "Here is the golden rule of MongoDB: A single BSON document cannot exceed sixteen megabytes. If you embed "
            "every user comment inside a blog post document, when that post gets one hundred thousand comments, the "
            "document hits the limit and write operations crash! Always reference comments in a separate collection."
        )
    },
    # 08:00 PM IST
    {
        "hour_ist": 20,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "DELETE vs TRUNCATE vs DROP in SQL (FAANG Classic) #Shorts #SQL",
        "badge": "FAANG SQL INTERVIEW • DAY 1",
        "hook_text": "What is the exact difference between DELETE, TRUNCATE, and DROP?",
        "code": "-- DELETE: Slow, logged per row, rollbackable\nDELETE FROM logs WHERE id = 1;\n\n-- TRUNCATE: Fast, deallocates pages\nTRUNCATE TABLE temp;\n\n-- DROP: Destroys data AND schema\nDROP TABLE old;",
        "caption": "DML vs DDL Operations Explained",
        "riddle_text": "Bookmark This Cheat Sheet 📌",
        "speech": (
            "Here is a classic database interview question: What is the difference between DELETE, TRUNCATE, and DROP? "
            "DELETE removes rows one by one and can be rolled back. TRUNCATE is a DDL command that deallocates all disk pages "
            "instantly, making it hundreds of times faster. And DROP wipes out both the data and the table schema permanently!"
        )
    },
    # 09:00 PM IST
    {
        "hour_ist": 21,
        "track": "python",
        "playlist_key": "python_shorts",
        "title": "FAANG Interview: Is Python Call-by-Value or Reference? #Shorts #Python",
        "badge": "FAANG PYTHON INTERVIEW • DAY 1",
        "hook_text": "Is Python Call-by-Value or Call-by-Reference? (90% Fail This!)",
        "code": "def modify(x):\n    x.append(99)\n\nlst = [1, 2]\nmodify(lst)\nprint(lst) # [1, 2, 99]! Mutated!",
        "caption": "It is Call-by-Object-Sharing!",
        "riddle_text": "Pointers are Passed by Value 🎯",
        "speech": (
            "Is Python call-by-value or call-by-reference? The answer is neither! Python uses call-by-object-sharing. "
            "The memory address of the object is passed by value. If you mutate a mutable object like a list inside "
            "the function, the caller sees the change. But reassigning the variable does not affect the caller."
        )
    },
    # 10:00 PM IST
    {
        "hour_ist": 22,
        "track": "java",
        "playlist_key": "java_shorts",
        "title": "Can You Run Java Code Without a main() Method? #Shorts #Java",
        "badge": "JAVA INTERVIEW RIDDLE • DAY 1",
        "hook_text": "Can you execute Java code without a public static void main method?",
        "code": "public class Secret {\n    static {\n        System.out.println(\"Runs BEFORE main()!\");\n    }\n}",
        "caption": "Static Initialization Blocks Run at Class Load!",
        "riddle_text": "JVM ClassLoader Magic ✨",
        "speech": (
            "Can you run code in Java without a main method? Yes, using static initialization blocks! When the JVM "
            "ClassLoader loads a class, static blocks execute immediately before any methods are invoked. Libraries "
            "use this to configure database drivers and system drivers at startup. Subscribe for more Java secrets!"
        )
    },
    # 11:00 PM IST
    {
        "hour_ist": 23,
        "track": "sql",
        "playlist_key": "sql_shorts",
        "title": "The Orphaned Row Disaster: ON DELETE CASCADE #Shorts #SQL",
        "badge": "SQL RELATIONAL DESIGN • DAY 1",
        "hook_text": "Why deleting a customer without Foreign Keys ruins your database",
        "code": "-- Foreign Key with Cascade\nCREATE TABLE orders (\n    id INT PRIMARY KEY,\n    customer_id INT REFERENCES customers(id)\n        ON DELETE CASCADE\n);",
        "caption": "Maintain Relational Integrity Cleanly",
        "riddle_text": "Zero Orphaned Ghost Records 🛡️",
        "speech": (
            "What happens when a user deletes their account, but their orders remain in your database forever? Those are "
            "orphaned ghost rows. By defining Foreign Keys with ON DELETE CASCADE, deleting a customer automatically cleans "
            "up their related records, keeping your relational database pristine. Day 2 drops tomorrow at six PM!"
        )
    }
]
