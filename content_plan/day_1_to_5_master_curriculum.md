# 🎓 60-Day Tech Masterclass: Days 1 to 5 Content Blueprint

> **Schedule Matrix (IST):**
> * 🐍 **10:00 AM:** Python Masterclass (10–15 min PPT Animation)
> * ☕ **12:00 PM:** Java Masterclass (10–15 min PPT Animation)
> * 🍃 **02:00 PM:** MongoDB Masterclass (10–15 min PPT Animation)
> * 🗄️ **06:00 PM:** SQL Masterclass (10–15 min PPT Animation)
> * 📱 **Hourly:** 24 Curated Shorts (6 per track per day)

---

# 📅 DAY 1: Foundation, Architecture & Memory Models

## 🐍 10:00 AM — Python Masterclass (Ep 1)
* **Title:** *How Python Actually Manages Memory (Variables, Pointers & The Stack/Heap)*
* **Target Duration:** 11:30
* **Real-World Analogy:** A library where sticky notes (variables) point to books on shelves (objects). You don't copy the book; you just write the shelf number on another sticky note.
* **PPT Slide Deck Breakdown:**
  * **Slide 1 (Title):** Modern dark slide with glowing Python badge. *"Everything in Python is an Object."*
  * **Slide 2 (Concept):** Animated memory diagram. The variable name on the Stack pointing via an arrow to memory block on Heap.
  * **Slide 3 (Interactive Code):** `a = [1, 2]`, `b = a`, `b.append(3)`. Visualizing why `a` changes too!
  * **Slide 4 (The Trap / Anti-Pattern):** Mutable Default Arguments (`def append_to(element, target=[]):`). Showing the shared list bug in production microservices.
  * **Slide 5 (Pro Fix):** Using `target=None` and `if target is None: target = []`.
  * **Slide 6 (FAANG Interview Challenge):** What is the exact difference between `is` (identity via `id()`) and `==` (equality via `__eq__`)?

### 📱 Day 1: Python Shorts (6 Episodes)
1. **08:00 AM [Teaser]:** *"Why `a = b` in Python will break your production code at 2 AM..."* (Funnels to 10 AM Long Video).
2. **09:00 AM [Output Riddle]:** `x = 256; y = 256; print(x is y)` vs `x = 257; y = 257; print(x is y)`. Why does Python say `True` then `False`? (Small integer caching).
3. **03:00 PM [Pro Tip]:** The 1-line Python swap: `a, b = b, a` — Animated stack frame showing tuple packing/unpacking under the hood.
4. **07:00 PM [Spot the Bug]:** A function with `def add_item(item, box=[])` that remembers previous users' items!
5. **09:00 PM [FAANG Q]:** *"Is Python call-by-value or call-by-reference?"* (Answer: Call by object reference / sharing).
6. **10:30 PM [Homework Recap]:** Visual solution to Day 1's memory pointer riddle.

---

## ☕ 12:00 PM — Java Masterclass (Ep 1)
* **Title:** *Inside the JVM: How Bytecode, ClassLoader & Memory Actually Run*
* **Target Duration:** 12:45
* **Real-World Analogy:** An architect blueprint (Java Source Code `.java`), converted to standardized factory instructions (Bytecode `.class`), executed by a specialized local machine (JVM with JIT Compiler).
* **PPT Slide Deck Breakdown:**
  * **Slide 1 (Title):** Blue/Orange gradient slide. *"Write Once, Run Anywhere: The True Cost & Genius of the JVM."*
  * **Slide 2 (Concept):** 3-stage animated workflow: Source Code $\rightarrow$ `javac` $\rightarrow$ Bytecode $\rightarrow$ JVM (ClassLoader, Runtime Data Area, Execution Engine).
  * **Slide 3 (Memory Map):** Animated Stack (primitive types, method frames) vs Heap (objects, String Constant Pool).
  * **Slide 4 (The Trap / Anti-Pattern):** Creating Strings with `new String("hello")` vs `"hello"`. Why `new` wastes Heap memory by bypassing the String Constant Pool.
  * **Slide 5 (Pro Fix):** String immutability and memory optimization with `StringBuilder` for concatenation loops.
  * **Slide 6 (Interview Challenge):** *"Can we run a Java program without `public static void main`?"* (Static initializer blocks in older JVMs vs Java 21 instance main).

### 📱 Day 1: Java Shorts (6 Episodes)
1. **11:00 AM [Teaser]:** *"Why banks still run on Java after 30 years (The JVM secret)."* (Funnels to 12 PM Long Video).
2. **11:30 AM [Memory Gotcha]:** `String s1 = "Java"; String s2 = "Java"; String s3 = new String("Java");` — `s1 == s2` vs `s1 == s3`.
3. **03:30 PM [Code Trick]:** Why `Integer.valueOf(100) == Integer.valueOf(100)` is `True`, but `1000 == 1000` is `False`! (Byte cache -128 to 127).
4. **07:30 PM [Spot the Bug]:** Forgetting that arrays in Java are fixed size; trying `arr[arr.length] = x`.
5. **09:30 PM [FAANG Q]:** *"What is the exact purpose of `static` in `public static void main`?"*
6. **11:00 PM [Tomorrow Preview]:** Preview of Primitive Data Types and Stack vs Heap memory frames.

---

## 🍃 02:00 PM — MongoDB Masterclass (Ep 1)
* **Title:** *SQL vs NoSQL: When & Why Modern Systems Choose MongoDB*
* **Target Duration:** 10:50
* **Real-World Analogy:** A filing cabinet with strict standardized folders with rigid columns (SQL Table) vs a flexible digital binder containing JSON documents with dynamic fields (MongoDB Collection).
* **PPT Slide Deck Breakdown:**
  * **Slide 1 (Title):** Emerald dark aesthetic. *"Beyond Rows and Tables: Thinking in Documents & BSON."*
  * **Slide 2 (Concept):** Anatomy of a Document: `_id` (12-byte hex ObjectId), key-value pairs, nested sub-documents, and arrays.
  * **Slide 3 (Interactive Code):** Inserting a real e-commerce order document with embedded items vs 3 normalized SQL tables.
  * **Slide 4 (The Trap / Anti-Pattern):** Treating MongoDB like SQL by creating 20 tiny collections and doing client-side joins.
  * **Slide 5 (Pro Fix):** The golden rule of document modeling: *"Data that is accessed together should be stored together."*
  * **Slide 6 (Interview Challenge):** *"What is BSON and why didn't MongoDB just use pure JSON?"* (BSON adds binary data, date types, and fast traversal headers).

### 📱 Day 1: MongoDB Shorts (6 Episodes)
1. **01:00 PM [Teaser]:** *"Why Amazon and Uber switched key microservices to NoSQL documents."* (Funnels to 2 PM Long Video).
2. **01:30 PM [Quick Comparison]:** SQL Table vs MongoDB Collection in 30 seconds (Venn diagram animation).
3. **04:00 PM [Hidden Feature]:** What is inside an `ObjectId("672...")`? (4-byte timestamp + 5-byte random + 3-byte counter).
4. **08:30 PM [Spot the Bug]:** Trying to save a single MongoDB document larger than 16MB (The BSON document size limit).
5. **10:00 PM [Micro System Design]:** Storing user shopping cart: SQL multi-table join vs 1 single Mongo document.
6. **11:15 PM [Riddle]:** Can MongoDB be ACID compliant? (Yes! Multi-document transactions introduced in Mongo 4.0).

---

## 🗄️ 06:00 PM — SQL Masterclass (Ep 1)
* **Title:** *The Relational Blueprint: ACID Transactions, Schemas & Table Constraints*
* **Target Duration:** 11:15
* **Real-World Analogy:** A bank ledger: if you transfer \$100 from Account A to Account B, both the debit and credit must succeed together. If the power cuts mid-way, the ledger rolls back completely (Atomicity).
* **PPT Slide Deck Breakdown:**
  * **Slide 1 (Title):** Cobalt navy slide. *"The Foundation of Enterprise Data: ACID & Relational Integrity."*
  * **Slide 2 (Concept):** Breakdown of ACID (Atomicity, Consistency, Isolation, Durability) with animated bank ledger graphics.
  * **Slide 3 (Interactive Code):** `CREATE TABLE users` with `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, and `DEFAULT`.
  * **Slide 4 (The Trap / Anti-Pattern):** Using `CHAR(255)` instead of `VARCHAR(255)`, and omitting foreign key constraints leading to orphaned database rows.
  * **Slide 5 (Pro Fix):** Foreign keys with `ON DELETE CASCADE` vs `ON DELETE RESTRICT` explained visually with connected parent-child boxes.
  * **Slide 6 (Interview Challenge):** *"Can a relational table have multiple Primary Keys? What is a Composite Key vs a Candidate Key?"*

### 📱 Day 1: SQL Shorts (6 Episodes)
1. **05:00 PM [Teaser]:** *"What happens when a database crashes during a \$10,000 money transfer?"* (Funnels to 6 PM Long Video).
2. **05:30 PM [Riddle]:** Primary Key vs Unique Key — What is the one crucial difference? (A table can have multiple Unique keys and allow `NULL`).
3. **06:45 PM [Syntax Trick]:** Using `CHECK (age >= 18)` to enforce business rules directly at the database engine level.
4. **08:00 PM [Spot the Bug]:** Inserting a foreign key referencing an ID that doesn't exist in the parent table.
5. **09:15 PM [FAANG Q]:** *"What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?"* (Rollback capability, speed, and schema destruction).
6. **10:45 PM [Recap]:** The 4 ACID rules visualized in 30 seconds.

---
---

# 📅 DAY 2: Data Structures, Types & Basic Querying

## 🐍 10:00 AM — Python: Lists, Tuples, Dictionaries & Sets
* **Topic:** The big 4 data structures: when to use each, memory footprints, and $O(1)$ vs $O(n)$ search speeds.
* **PPT Visuals:** Side-by-side memory layout (Contiguous array for List, Fixed size for Tuple, Hash Map for Dict/Set).
* **The Trap:** Using a `list` to check for membership `if item in large_list:` inside a loop ($O(n^2)$ performance kill).
* **Pro Fix:** Converting to a `set` for instant $O(1)$ lookup time.
* **6 Shorts:**
  * List vs Tuple memory benchmark
  * Why Dictionary keys must be immutable / hashable
  * The hidden speed of `set.intersection()`
  * Spot the Bug: Modifying a list while iterating over it
  * Interview Q: How does Python resolve hash collisions in dicts?
  * Day 2 Challenge: Deduplicate a list while preserving original order.

## ☕ 12:00 PM — Java: Primitives, Memory Allocation & Type Casting
* **Topic:** The 8 primitives (`byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char`), Autoboxing, and Widening vs Narrowing casting.
* **PPT Visuals:** Animated byte grids showing overflow when casting `int 130` to `byte` (-126).
* **The Trap:** Silent numeric overflow in calculations like `long millis = 24 * 60 * 60 * 1000 * 1000;` (calculates as 32-bit `int` before assigning).
* **Pro Fix:** Appending `L` literal to enforce 64-bit math.
* **6 Shorts:**
  * Why `float` and `double` are forbidden in banking calculations (`BigDecimal` demo)
  * Java Byte Overflow Riddle (`byte b = 127; b++; print(b)`)
  * Autoboxing performance hit in 100,000 iterations
  * Spot the Bug: `char` arithmetic unexpected integer conversion
  * Interview Q: Why does Java not have unsigned integers?
  * Day 2 Challenge: Parse an integer safely without throwing `NumberFormatException`.

## 🍃 02:00 PM — MongoDB: CRUD Mastery (`insert`, `find`, `projection`)
* **Topic:** Reading and filtering documents: `find()`, `findOne()`, query criteria, and exact field Projections (`{ name: 1, _id: 0 }`).
* **PPT Visuals:** Document pipeline funneling raw database records through a projection mask.
* **The Trap:** Fetching full 2MB documents over the network when the UI only needs 2 fields.
* **Pro Fix:** Strict projection to optimize network throughput and RAM.
* **6 Shorts:**
  * Difference between `insert()` (deprecated), `insertOne()`, and `insertMany()`
  * Why does MongoDB return `_id` by default even when you ask for specific fields?
  * Fast querying on nested fields with dot notation (`"address.city": "Mumbai"`)
  * Spot the Bug: Case sensitivity in string queries
  * Interview Q: How does MongoDB cursor pagination (`limit` & `skip`) work under the hood?
  * Day 2 Challenge: Write a query to find all users with age $> 21$ returning only their emails.

## 🗄️ 06:00 PM — SQL: Filtering Power (`SELECT`, `WHERE`, `LIKE`, `IN`, `BETWEEN`)
* **Topic:** The SQL query execution order (How SQL executes `FROM` first, then `WHERE`, and `SELECT` near the end).
* **PPT Visuals:** Step-by-step query execution lifecycle animation.
* **The Trap:** Using `WHERE column LIKE '%search%'` which forces a full table scan and disables index seeks.
* **Pro Fix:** Prefix search `LIKE 'search%'` or Full-Text search indexes.
* **6 Shorts:**
  * The actual order SQL executes: Why you cannot use a `SELECT` alias in a `WHERE` clause!
  * `NULL = NULL` is False! (Why `IS NULL` is required)
  * `IN` operator vs multiple `OR` statements performance comparison
  * Spot the Bug: Operator precedence with `AND` and `OR` without parentheses
  * Interview Q: What is the difference between `COUNT(*)`, `COUNT(1)`, and `COUNT(column)`?
  * Day 2 Challenge: Retrieve top 5 highest earners excluding sales department.

---
---

# 📅 DAY 3: Control Flow, Iteration & Aggregations

## 🐍 10:00 AM — Python: List Comprehensions, `zip()`, `enumerate()` & Iterators
* **Topic:** Writing idiomatic Python without nested C-style index loops.
* **PPT Visuals:** Visual transformer taking a raw list through an inline filter/map pipeline.
* **The Trap:** Writing massive, 4-tier nested list comprehensions that no teammate can read.
* **Pro Fix:** Generator expressions `(x for x in data)` for multi-gigabyte files to avoid `MemoryError`.
* **6 Shorts:**
  * `range(len(arr))` vs `enumerate(arr)` speed & readability duel
  * Pairing two lists with `zip(names, scores)` and handling uneven lengths with `zip_longest`
  * List comprehension vs Generator memory test (4 MB vs 128 bytes)
  * Spot the Bug: Variable leaking outside list comprehension in Python 2 vs 3
  * Interview Q: What is the Iterator protocol (`__iter__` and `__next__`)?
  * Day 3 Challenge: Flatten a 2D matrix into a 1D list in one single line.

## ☕ 12:00 PM — Java: Loops, Modern `switch` Expressions & Control Flow
* **Topic:** Traditional `for` vs Enhanced `for-each`, labeled `break`, and the new pattern-matching `switch` in Java 17/21.
* **PPT Visuals:** Decision tree animation showing modern `switch` arrow syntax with direct expression returns.
* **The Trap:** The classic missing `break` in traditional switch causing accidental fall-through bugs.
* **Pro Fix:** Arrow syntax `case A -> result;` which has zero fall-through and supports yield.
* **6 Shorts:**
  * The forgotten Java feature: Labeled `break` to exit nested loops cleanly
  * Traditional `switch` vs Java 21 Pattern Matching `switch`
  * Why modifying a collection inside a `for-each` loop throws `ConcurrentModificationException`
  * Spot the Bug: `while(i < 10);` with an accidental semicolon!
  * Interview Q: Is `for(;;)` faster than `while(true)` in Java?
  * Day 3 Challenge: Write a clean fizzbuzz without if-else statements.

## 🍃 02:00 PM — MongoDB: Advanced Comparison & Logical Operators
* **Topic:** Filtering with `$gt`, `$gte`, `$lt`, `$in`, `$nin`, `$and`, `$or`, and `$nor`.
* **PPT Visuals:** Boolean logic gates animating document filtration based on complex rules.
* **The Trap:** Redundantly wrapping implicit `$and` conditions inside an explicit `$and: [...]` array.
* **Pro Fix:** Composing concise queries using MongoDB's implicit multi-field and.
* **6 Shorts:**
  * `$in` vs `$or`: Which operator does MongoDB optimize faster?
  * Querying arrays with `$all` vs `$in` (Matching full set vs any single element)
  * The `$exists` operator: Finding documents where a field is missing altogether
  * Spot the Bug: Querying an array of numbers with `$gt` and `$lt` simultaneously
  * Interview Q: How does MongoDB handle queries on fields that have null values?
  * Day 3 Challenge: Find all products with rating $\ge 4.5$ AND priced under \$50 OR in category "Electronics".

## 🗄️ 06:00 PM — SQL: Grouping & Aggregates (`GROUP BY`, `HAVING`, `SUM`, `AVG`)
* **Topic:** Data summarization: Calculating totals, averages, and the crucial distinction between `WHERE` and `HAVING`.
* **PPT Visuals:** Aggregation bucket animation: rows sorting into category bins and collapsing into scalar metrics.
* **The Trap:** Filtering aggregate values using `WHERE SUM(sales) > 1000` (throws SQL syntax error).
* **Pro Fix:** Filtering individual rows with `WHERE` *before* grouping, and filtering aggregated groups with `HAVING`.
* **6 Shorts:**
  * The \#1 SQL Interview Question: `WHERE` vs `HAVING` in 30 seconds
  * How `COUNT(column)` ignores `NULL`s, but `COUNT(*)` counts the row
  * Grouping by multiple columns: How SQL creates multi-level hierarchies
  * Spot the Bug: Selecting non-aggregated columns without putting them in `GROUP BY`
  * Interview Q: Can you use `HAVING` without a `GROUP BY` clause?
  * Day 3 Challenge: Find departments with more than 5 employees and average salary $> \$80,000$.

---
---

# 📅 DAY 4: Functions, Methods, Scopes & Core Updates

## 🐍 10:00 AM — Python: Functions, Scopes (`LEGB`), `*args`, `**kwargs` & Lambdas
* **Topic:** First-class functions, closures, dynamic argument unpacking, and understanding variable lookup scopes.
* **PPT Visuals:** Nested scope circles: Local $\rightarrow$ Enclosing $\rightarrow$ Global $\rightarrow$ Built-in (`LEGB`).
* **The Trap:** Trying to modify a global variable inside a function without the `global` keyword (`UnboundLocalError`).
* **Pro Fix:** Pure functions with explicit return values rather than mutating global state.
* **6 Shorts:**
  * Unpacking magic: `*` and `**` explained in 45 seconds
  * Why you should almost never use `global` in professional code
  * Lambda functions: When to use them and when `def` is 10x better
  * Spot the Bug: Late binding closures in a list of lambdas (`[lambda: i for i in range(3)]`)
  * Interview Q: What is the difference between an argument and a parameter?
  * Day 4 Challenge: Write a function that accepts any number of positional and keyword arguments and returns their count.

## ☕ 12:00 PM — Java: Methods, Parameter Passing & Method Overloading
* **Topic:** Pass-by-value in Java, variable arguments (`varargs`), method signatures, and overloading rules.
* **PPT Visuals:** Stack frame creation during method calls, showing object references passed by value.
* **The Trap:** Assuming Java passes objects "by reference" and trying to reassign an object reference inside a helper method.
* **Pro Fix:** Mutating object state via setters rather than reassigning parameter references.
* **6 Shorts:**
  * Proving once and for all: Java is STRICTLY Pass-by-Value!
  * Method Overloading vs Overriding visual battle
  * Varargs under the hood: How `String... args` creates a hidden array
  * Spot the Bug: Ambiguous method call with overloaded `null` arguments (`foo(String s)` vs `foo(Integer i)`)
  * Interview Q: Can we overload the `main` method in Java?
  * Day 4 Challenge: Create an overloaded math utility with automatic widening support.

## 🍃 02:00 PM — MongoDB: Document Updates (`$set`, `$inc`, `$push`, `upsert`)
* **Topic:** Atomic document modifications without rewriting the whole document.
* **PPT Visuals:** Surgical update animation showing MongoDB modifying a single key in-place on disk.
* **The Trap:** Using `replaceOne()` when you meant to update a single field (accidentally wiping out the rest of the document!).
* **Pro Fix:** Always using update operators like `$set` or `$inc` to preserve existing fields.
* **6 Shorts:**
  * `$set` vs Direct Object Update: The mistake that wipes out production collections
  * Atomic counters with `$inc`: Preventing race conditions during inventory checkout
  * Array manipulation: `$push`, `$pull`, and `$addToSet` (preventing duplicates)
  * Spot the Bug: Forgetting `{ multi: true }` or using `updateMany` for batch operations
  * Interview Q: What is an `upsert` and how does it prevent race conditions?
  * Day 4 Challenge: Increment a user's login count, update their last active date, and add an IP address to their history array in one atomic query.

## 🗄️ 06:00 PM — SQL: Mastering `INNER JOIN` & `LEFT JOIN`
* **Topic:** Combining relational data across multiple tables using foreign key relationships.
* **PPT Visuals:** Interactive Venn diagrams and side-by-side row matching animation showing how matching rows merge.
* **The Trap:** Filtering the right table in a `LEFT JOIN`'s `WHERE` clause (accidentally turning it into an `INNER JOIN`!).
* **Pro Fix:** Placing right-table filter conditions directly inside the `ON` clause.
* **6 Shorts:**
  * `INNER JOIN` vs `LEFT JOIN` visualized with animated Venn circles
  * The catastrophic Cartesian product: What happens when you forget the `ON` clause!
  * `JOIN` on multiple conditions: Joining on composite keys
  * Spot the Bug: `NULL` checking on `LEFT JOIN`ed tables in `WHERE`
  * Interview Q: What is faster: A `JOIN` or a Subquery?
  * Day 4 Challenge: Write a query to find all customers who have NEVER placed an order (`LEFT JOIN ... WHERE order.id IS NULL`).

---
---

# 📅 DAY 5: Object-Oriented Programming & Advanced Joins

## 🐍 10:00 AM — Python: OOP Foundations (Classes, Instances, `__init__`, `self`)
* **Topic:** Object-Oriented design in Python: Class attributes vs Instance attributes, dunder methods, and the `self` parameter.
* **PPT Visuals:** A factory blueprint stamping out independent vehicle objects in memory.
* **The Trap:** Defining a mutable class attribute (`class Dog: tricks = []`) where all dog instances share the same tricks list!
* **Pro Fix:** Initializing instance attributes strictly inside `__init__(self)`.
* **6 Shorts:**
  * What actually is `self` in Python? (The explicit instance reference)
  * Class Variables vs Instance Variables trap that ruins microservices
  * The magic of `__str__` vs `__repr__` for clean debugging
  * Spot the Bug: Forgetting `self.` when accessing instance methods
  * Interview Q: Can you add attributes to a Python class dynamically at runtime? (Monkey patching)
  * Day 5 Challenge: Create a `BankAccount` class with encapsulation for balance checking.

## ☕ 12:00 PM — Java: OOP Foundations (Encapsulation, Constructors, `this`)
* **Topic:** The first pillar of OOP: Data hiding with `private` fields, public getters/setters, constructor overloading, and constructor chaining with `this()`.
* **PPT Visuals:** A secure vault object: outside callers can only interact via the keypad (public methods), not reach inside directly.
* **The Trap:** Returning direct mutable references from getters (e.g. `public Date getDob() { return this.dob; }`), allowing callers to alter internal state.
* **Pro Fix:** Returning defensive copies in getters.
* **6 Shorts:**
  * Why all fields in Java should be `private`: Encapsulation in 45s
  * Constructor chaining with `this()`: Writing clean, DRY constructors
  * Default constructor myth: What happens when you define a parameterized constructor?
  * Spot the Bug: Shadowing instance variables by forgetting `this.name = name`
  * Interview Q: What is the difference between Shallow Copy and Deep Copy in Java?
  * Day 5 Challenge: Implement an immutable class in Java with defensive copying.

## 🍃 02:00 PM — MongoDB: Schema Design (Embedding vs Referencing)
* **Topic:** 1-to-1 and 1-to-Many data relationships: When to nest documents inside arrays vs when to use separate collections and DBRefs.
* **PPT Visuals:** Side-by-side architecture comparison: Single nested document vs 2 linked collections.
* **The Trap:** Unbounded array growth! Storing 500,000 comments directly inside a single blog post document until it exceeds the 16MB limit.
* **Pro Fix:** Hybrid modeling: Embedding the top 10 most recent comments, and referencing the rest in a `comments` collection.
* **6 Shorts:**
  * When to Embed vs When to Reference in MongoDB (The 3 golden rules)
  * The 16MB limit horror story: How unbounded arrays crash production databases
  * 1-to-Squillions relationship: Why parent-referencing is the only safe way
  * Spot the Bug: Trying to do multi-level deep nested queries on unbounded arrays
  * Interview Q: Does MongoDB have Foreign Keys? How does `$lookup` simulate joins?
  * Day 5 Challenge: Design a production MongoDB schema for an Instagram post with likes and comments.

## 🗄️ 06:00 PM — SQL: Advanced `JOINs` (`RIGHT`, `FULL OUTER`, `CROSS` & Self Joins)
* **Topic:** Completing the JOIN toolkit: Outer relationships, matrix multiplications with `CROSS JOIN`, and hierarchical queries using `Self Joins`.
* **PPT Visuals:** Animated grid showing Employee table joining with itself to display Employee $\rightarrow$ Manager hierarchy.
* **The Trap:** Running an unconstrained `CROSS JOIN` between two tables of 100,000 rows, creating a 10-billion row explosion that crashes the server.
* **Pro Fix:** Always pairing Cartesian joins with specific constraint conditions or small lookup tables.
* **6 Shorts:**
  * What is a Self Join? Modeling Employee $\rightarrow$ Manager hierarchies in 45s
  * `RIGHT JOIN` vs `LEFT JOIN`: Why senior SQL developers almost never write `RIGHT JOIN`
  * `FULL OUTER JOIN`: Catching non-matching records on both sides
  * Spot the Bug: Joining a table to itself without table aliases (`e1` and `e2`)
  * Interview Q: How would you find duplicate records in a table using a Self Join?
  * Day 5 Challenge: Write a single query to list all employees whose salary is higher than their direct manager's salary.
