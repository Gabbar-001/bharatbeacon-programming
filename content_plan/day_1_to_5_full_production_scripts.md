# 🎬 Full 5-Day Production Delivery Blueprint (Masterclasses & Shorts)

This document contains the **exact script outlines, visual slide animations, live code demonstrations, anti-pattern traps, and FAANG interview challenges** for all **20 Long-Form Masterclasses** and **120 Viral Shorts** across Days 1 through 5.

---

# 📅 DAY 1: Foundation, Architecture & Memory Models

---

## 🐍 10:00 AM — Python Masterclass (Episode 1)
* **Title:** *How Python Actually Manages Memory (Variables, Pointers & The Stack/Heap)*
* **Target Runtime:** 11:30 | **Format:** 16:9 Presentation + Interactive Code Sandbox

### Scene Breakdown & Presentation Script:
* **Scene 1 [00:00 - 01:45] The Hook & Real-World Analogy:**
  * *Narration:* "Welcome to Day 1 of our Python Masterclass! Most programmers think a variable in Python is a box that holds a number. That mental model is dead wrong—and it causes catastrophic memory leaks in production microservices. In Python, variables are not boxes; they are sticky notes pointing to objects floating in memory."
  * *PPT Animation:* Visual of an Amazon warehouse shelf (The Heap). A box containing the number `42` sits on the shelf. Variable `x` is shown as a glowing sticky note sticking a reference tag to that box.
* **Scene 2 [01:45 - 04:30] The Pointer Trap (Interactive Code):**
  * *Narration:* "Watch what happens when we assign list `a` to list `b`. You think you copied the list? Let's check memory addresses using `id()`."
  * *Code on Screen (Tokyo Night IDE):*
    ```python
    a = [1, 2, 3]
    b = a  # Does NOT copy the list!
    b.append(99)

    print(f"a: {a}")  # Output: [1, 2, 3, 99]
    print(f"id(a) == id(b): {id(a) == id(b)}")  # True!
    ```
  * *PPT Animation:* An arrow connects `a` and `b` to the exact same memory block `0x7ffe9a2`. Appending to `b` alters `a` instantly.
* **Scene 3 [04:30 - 07:30] The Production Anti-Pattern: Mutable Default Arguments:**
  * *Narration:* "Here is the rookie bug that takes down production web apps. Look at this user registration function:"
  * *Anti-Pattern Code:*
    ```python
    # ❌ THE ROOKIE TRAP
    def create_user_profile(username, permissions=[]):
        permissions.append("read")
        return {"user": username, "perms": permissions}

    user1 = create_user_profile("admin")
    user2 = create_user_profile("guest")
    print(user2["perms"])  # ['read', 'read']! Guest inherited admin's permissions!
    ```
  * *PPT Animation:* Red alert flashing: Python defines default arguments once when the module loads, not every time the function is called! All users share the same list instance.
* **Scene 4 [07:30 - 09:30] The Pro Industry Fix:**
  * *Clean Code:*
    ```python
    # ✅ THE INDUSTRY PRO WAY
    def create_user_profile(username, permissions=None):
        if permissions is None:
            permissions = []
        permissions.append("read")
        return {"user": username, "perms": permissions}
    ```
  * *PPT Animation:* A new fresh list is created inside the function scope for each caller.
* **Scene 5 [09:30 - 11:30] FAANG Interview Challenge & Day 1 Homework:**
  * *Interview Riddle:* "What is Small Integer Caching in Python? Why does `x = 256; y = 256; x is y` return `True`, but `x = 257; y = 257; x is y` return `False`?"
  * *Takeaway:* Python pre-allocates small integers between $-5$ and $256$ in memory at startup for speed.
  * *Homework:* Drop your answer in the comments: How do you make a true deep copy of a nested list?

---

## ☕ 12:00 PM — Java Masterclass (Episode 1)
* **Title:** *Inside the JVM: Bytecode, ClassLoader & Memory Architecture*
* **Target Runtime:** 12:15 | **Format:** 16:9 Animated Architectural Diagram + IDE Sandbox

### Scene Breakdown & Presentation Script:
* **Scene 1 [00:00 - 02:00] The Billion-Device Secret:**
  * *Narration:* "Ever wondered why global banks, NASA, and Android still run on Java? The secret isn't the syntax—it's the virtual machine. Today, we step inside the Java Virtual Machine to see what actually happens to your code."
  * *PPT Animation:* Three-tier architectural workflow: `.java` Source $\rightarrow$ `javac` compiler $\rightarrow$ `.class` Bytecode $\rightarrow$ JVM ClassLoader Subsystem.
* **Scene 2 [02:00 - 05:30] Stack vs Heap Memory Frames:**
  * *Narration:* "Every thread gets its own Stack memory for method execution and local primitive variables. But every object you instantiate lives on the shared Heap."
  * *PPT Animation:* Split-screen memory visualizer. Left: Stack frames pushing and popping. Right: Heap objects being tracked by the Garbage Collector.
* **Scene 3 [05:30 - 08:30] The String Constant Pool & Memory Wastage:**
  * *Narration:* "Look at how Strings are created. Do not use the `new` keyword for Strings unless you want to throw your company's server memory in the trash."
  * *Code on Screen:*
    ```java
    String s1 = "Bharat";
    String s2 = "Bharat";
    String s3 = new String("Bharat");

    System.out.println(s1 == s2);      // true (Points to same String Constant Pool object)
    System.out.println(s1 == s3);      // false (Bypasses pool, creates separate Heap object!)
    System.out.println(s1.equals(s3)); // true (Compares values, not references)
    ```
* **Scene 4 [08:30 - 10:30] The Production Anti-Pattern: String Concatenation in Loops:**
  * *Narration:* "Strings in Java are immutable. Writing `s += "data"` inside a 10,000-iteration loop creates 10,000 dead objects on the Heap, triggering Garbage Collection freezes."
  * *Pro Fix:* Use `StringBuilder` with pre-allocated buffer capacity.
* **Scene 5 [10:30 - 12:15] FAANG Interview Challenge:**
  * *Interview Riddle:* "Can you execute code in Java without a `main` method? (Answer: Static initializer blocks run at class-loading time before `main` is ever invoked!)."

---

## 🍃 02:00 PM — MongoDB Masterclass (Episode 1)
* **Title:** *Beyond Rows & Tables: Thinking in Documents & BSON*
* **Target Runtime:** 10:45 | **Format:** 16:9 Document Pipeline + Compass/Mongo Shell Sandbox

### Scene Breakdown & Presentation Script:
* **Scene 1 [00:00 - 02:00] The Uber / Netflix Problem:**
  * *Narration:* "Why did modern tech companies migrate their core apps from traditional SQL to MongoDB? Because the real world doesn't look like flat spreadsheet rows. Real-world data is nested, hierarchical, and dynamic."
  * *PPT Animation:* An Uber trip: Rider profile, driver rating, pickup GPS coordinates, and payment info—shown as 1 unified JSON document vs 5 split SQL tables.
* **Scene 2 [02:00 - 05:00] BSON Under the Hood:**
  * *Narration:* "MongoDB doesn't store plain JSON on disk. It stores BSON (Binary JSON). Why? BSON adds critical data types like 64-bit integers, raw dates, and binary headers that let the database jump straight to a specific key without scanning the whole document."
  * *PPT Visual:* An animated `ObjectId("672f0...")` dissecting its 12 bytes: 4 bytes Unix timestamp + 5 bytes random process identifier + 3 bytes increment counter.
* **Scene 3 [05:00 - 07:30] Live CRUD: The First Document:**
  * *Mongo Shell Sandbox:*
    ```javascript
    db.courses.insertOne({
      title: "Full-Stack Bootcamp",
      technologies: ["Python", "Java", "MongoDB", "SQL"],
      duration_days: 60,
      active: true,
      created_at: new Date()
    });
    ```
* **Scene 4 [07:30 - 09:30] The Anti-Pattern: Over-Normalization:**
  * *Narration:* "The biggest mistake SQL developers make when switching to Mongo: creating 20 tiny collections and doing client-side joins. The Golden Rule of Document Design: Data that is read together must be stored together!"
* **Scene 5 [09:30 - 10:45] The 16MB Hard Limit:**
  * *Challenge:* A single MongoDB document cannot exceed 16MB. Never store an unbounded array of infinite user comments inside a single blog post document!

---

## 🗄️ 06:00 PM — SQL Masterclass (Episode 1)
* **Title:** *The Relational Blueprint: ACID Transactions, Schemas & Constraints*
* **Target Runtime:** 11:45 | **Format:** 16:9 Bank Ledger Visualization + PostgreSQL Terminal

### Scene Breakdown & Presentation Script:
* **Scene 1 [00:00 - 02:30] The \$10,000 Banking Crash:**
  * *Narration:* "Imagine transferring \$10,000 from your account to your friend's account. The bank deducts \$10,000 from you. Suddenly, the power cuts! What happened to your money? Relational databases were invented so this disaster can NEVER happen."
  * *PPT Animation:* Animated bank ledger showing ACID properties: Atomicity guarantees both debit and credit succeed together, or the entire transaction rolls back cleanly.
* **Scene 2 [02:30 - 05:30] The Anatomy of ACID:**
  * *Atomicity:* All-or-nothing execution via `COMMIT` and `ROLLBACK`.
  * *Consistency:* Database constraints (`NOT NULL`, `CHECK`) are never violated.
  * *Isolation:* Concurrent transactions do not read uncommitted "dirty" data.
  * *Durability:* Once committed, changes survive catastrophic system crashes via the Write-Ahead Log (WAL).
* **Scene 3 [05:30 - 08:30] Table Creation & Integrity Constraints (Live Sandbox):**
  * *SQL Sandbox:*
    ```sql
    CREATE TABLE bank_accounts (
        account_id SERIAL PRIMARY KEY,
        account_holder VARCHAR(100) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        balance NUMERIC(12, 2) CHECK (balance >= 0.00),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```
* **Scene 4 [08:30 - 10:30] The Trap: Orphaned Data & Missing Foreign Keys:**
  * *Narration:* "If you delete a customer from the customers table without foreign key constraints, their order records remain forever as ghost rows. Always define `ON DELETE CASCADE` or `ON DELETE RESTRICT`."
* **Scene 5 [10:30 - 11:45] Interview Challenge:**
  * *Interview Riddle:* "Can a relational table have multiple Primary Keys? (Answer: No, only ONE Primary Key per table, but that key can be a Composite Key made of multiple columns!)."

---

### 📱 Day 1: The 24 Viral Shorts Delivery Schedule

| Hour | Track | Format | Hook / Script Punchline | Call to Action |
| :---: | :---: | :---: | :--- | :--- |
| **07:30 AM** | 🐍 Python | Teaser | *"Why `a = b` in Python will silently destroy your database at 2 AM..."* | *"Full breakdown in Day 1 at 10 AM 👇"* |
| **08:15 AM** | 🐍 Python | Riddle | `x = 256; y = 256; x is y` is `True`. But `257 is 257` is `False`! What is happening? | *"Answer in pinned comment!"* |
| **09:00 AM** | 🐍 Python | Pro Tip | Swapping two numbers in 1 line: `a, b = b, a` without third variables. | *"Follow for daily Python clean code!"* |
| **10:45 AM** | 🐍 Python | Spot the Bug | `def add(val, l=[])` — Why does this function remember previous users? | *"Watch Day 1 for the fix!"* |
| **11:15 AM** | ☕ Java | Teaser | *"Why banks still pay \$200k for Java developers after 30 years."* | *"JVM Masterclass dropping at 12 PM 👇"* |
| **11:45 AM** | ☕ Java | Memory Gotcha | `s1 == s2` vs `s1 == new String("s")` — String Constant Pool in 40s. | *"Save this for your next interview!"* |
| **12:45 PM** | ☕ Java | Code Trick | Why `Integer.valueOf(100) == Integer.valueOf(100)` is `True` but `1000 == 1000` is `False`! | *"Byte cache explained!"* |
| **01:15 PM** | 🍃 Mongo | Teaser | *"Why Uber & Amazon tore down SQL tables for flexible JSON documents."* | *"MongoDB Masterclass at 2 PM 👇"* |
| **01:45 PM** | 🍃 Mongo | Comparison | SQL Table vs MongoDB Collection in 30 seconds (Venn diagram animation). | *"Which do you prefer? Vote below!"* |
| **02:45 PM** | 🍃 Mongo | Hidden Feature | What's actually hidden inside a MongoDB `ObjectId`? (Timestamp + Worker ID). | *"Drop a star on our GitHub repo!"* |
| **03:15 PM** | 🐍 Python | Interview Q | *"Is Python pass-by-value or pass-by-reference?"* (Neither! It's pass-by-object-sharing). | *"FAANG interview question solved."* |
| **03:45 PM** | ☕ Java | Interview Q | *"Why is `public static void main` required in Java?"* (Breakdown of each keyword). | *"Follow for Java mastery!"* |
| **04:15 PM** | 🍃 Mongo | Pro Tip | The 16MB document size limit horror story and how to avoid it. | *"Day 1 MongoDB lecture has more!"* |
| **05:00 PM** | 🗄️ SQL | Teaser | *"What happens when a database crashes mid-way through a \$10,000 wire transfer?"* | *"SQL ACID Masterclass at 6 PM 👇"* |
| **05:30 PM** | 🗄️ SQL | Riddle | Primary Key vs Unique Key: Can a Unique Key contain `NULL`? (Yes!). | *"Bookmark this cheat sheet!"* |
| **06:45 PM** | 🗄️ SQL | Syntax Trick | Using `CHECK (age >= 18)` to reject invalid data at the engine level. | *"Write cleaner SQL queries!"* |
| **07:15 PM** | 🗄️ SQL | Spot the Bug | Inserting a Foreign Key referencing an ID that doesn't exist in parent table. | *"Integrity constraint error solved."* |
| **07:45 PM** | 🐍 Python | Micro-Design | How Python stores variable references on Stack vs objects on Heap. | *"Part of our 60-day bootcamp."* |
| **08:15 PM** | ☕ Java | Spot the Bug | Fixed-size array trap: Trying to append past `arr.length`. | *"Use ArrayList instead!"* |
| **08:45 PM** | 🍃 Mongo | Micro-Design | Storing shopping carts: 1 Mongo document vs 4 SQL table joins. | *"NoSQL wins for read speed!"* |
| **09:15 PM** | 🗄️ SQL | FAANG Q | What is the real difference between `DELETE`, `TRUNCATE`, and `DROP`? | *"Save this interview classic!"* |
| **09:45 PM** | 🐍 Python | Homework | Day 1 Challenge: How to copy a nested list safely (`copy.deepcopy`). | *"Solution pinned in comments!"* |
| **10:15 PM** | ☕ Java | Riddle | Can you execute Java code without `main()`? (Static blocks!). | *"Java secret unlocked."* |
| **10:45 PM** | 🌟 Channel | Recap | Preview of Day 2: Lists, Java Primitives, CRUD queries & SQL `WHERE` clauses! | *"Subscribe for Day 2 tomorrow!"* |

---
---

# 📅 DAY 2: Data Structures, Types & Precision Filtering

---

## 🐍 10:00 AM — Python Masterclass (Episode 2)
* **Title:** *The Big 4 Data Structures: Lists, Tuples, Dictionaries & Sets ($O(1)$ vs $O(n)$)*
* **Visuals:** Animated time-complexity scale. Demonstrating why searching in a `list` takes linear time $O(n)$, while a `set` or `dict` takes instantaneous constant time $O(1)$ through hash table lookups.
* **The Code Sandbox:**
  ```python
  import time

  large_list = list(range(1_000_000))
  large_set = set(large_list)

  # List lookup: Checks every element one by one
  # Set lookup: Calculates hash and jumps directly to memory bucket
  ```
* **Anti-Pattern:** Using a `list` for frequent membership checks (`if user in user_list:`) inside a heavy loop.
* **Pro Fix:** Instantiating a `set` for lookup operations, cutting runtime from 12 seconds to 0.001 seconds.

---

## ☕ 12:00 PM — Java Masterclass (Episode 2)
* **Title:** *The 8 Primitive Data Types, Memory Allocation & The Float Precision Disaster*
* **Visuals:** Binary byte grids. Visualizing what happens when `byte b = 127; b++;` overflows to `-128`.
* **The Code Sandbox:**
  ```java
  // ❌ NEVER USE FLOAT FOR MONEY
  double a = 0.1 + 0.2;
  System.out.println(a); // 0.30000000000000004!

  // ✅ USE BIGDECIMAL IN ENTERPRISE BANKING
  BigDecimal b1 = new BigDecimal("0.1");
  BigDecimal b2 = new BigDecimal("0.2");
  System.out.println(b1.add(b2)); // 0.3
  ```
* **Anti-Pattern:** Calculating financial balances with `float` or `double`, leading to rounding discrepancies.

---

## 🍃 02:00 PM — MongoDB Masterclass (Episode 2)
* **Title:** *CRUD Mastery: `insertOne`, `find()`, and the Power of Projection*
* **Visuals:** Network throughput pipeline. Showing how projecting `{ title: 1, _id: 0 }` reduces network bandwidth by 95% compared to returning full 2MB documents.
* **The Code Sandbox:**
  ```javascript
  db.inventory.find(
    { status: "A", qty: { $lt: 30 } },
    { item: 1, qty: 1, _id: 0 } // Projection mask
  ).limit(10);
  ```
* **Anti-Pattern:** Fetching full heavy documents to the web server when the frontend only displays the username.

---

## 🗄️ 06:00 PM — SQL Masterclass (Episode 2)
* **Title:** *Query Execution Order & Smart Filtering (`SELECT`, `WHERE`, `LIKE`, `IN`, `BETWEEN`)*
* **Visuals:** The 6-stage SQL engine lifecycle animation: `FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `ORDER BY`.
* **The Code Sandbox:**
  ```sql
  SELECT employee_name, salary * 1.1 AS new_salary
  FROM employees
  WHERE department_id IN (10, 20, 30)
    AND hire_date BETWEEN '2024-01-01' AND '2024-12-31';
  ```
* **Anti-Pattern:** Trying to use `WHERE new_salary > 50000` (fails because `WHERE` runs *before* `SELECT` aliases exist!).
* **Shorts Highlights:** Why `NULL = NULL` is False (3-valued logic), `LIKE '%text%'` killing database indexes, and `COUNT(*)` vs `COUNT(column)`.

---
---

# 📅 DAY 3: Control Flow, Iterators & Aggregations

---

## 🐍 10:00 AM — Python Masterclass (Episode 3)
* **Title:** *Clean Python: List Comprehensions, `zip()`, `enumerate()` & Generators*
* **Visuals:** Inline stream transformer. Showing how traditional 6-line nested `for` loops collapse into clean, readable comprehensions.
* **The Code Sandbox:**
  ```python
  # ❌ ROOKIE C-STYLE LOOP
  for i in range(len(names)):
      print(f"{i}: {names[i]}")

  # ✅ CLEAN PYTHONIC ENUMERATE
  for i, name in enumerate(names, start=1):
      print(f"{i}: {name}")
  ```
* **Anti-Pattern:** Loading a 10GB CSV into memory with a list comprehension instead of using a Generator expression `(row for row in file)`.

---

## ☕ 12:00 PM — Java Masterclass (Episode 3)
* **Title:** *Modern Control Flow: Labeled Loops & Java 21 Pattern-Matching `switch`*
* **Visuals:** Arrow-style decision tree. Demonstrating the complete elimination of `break` statements with modern arrow syntax `case A -> result;`.
* **The Code Sandbox:**
  ```java
  // Modern Java Switch Expression (No fall-through bugs!)
  String dayType = switch (day) {
      case MONDAY, FRIDAY -> "Work day";
      case SATURDAY, SUNDAY -> "Weekend";
      default -> "Midweek";
  };
  ```
* **Anti-Pattern:** Removing items from a List during a `for-each` loop (triggers `ConcurrentModificationException`).

---

## 🍃 02:00 PM — MongoDB Masterclass (Episode 3)
* **Title:** *Complex Queries: Comparison, Logical & Array Operators (`$gt`, `$in`, `$all`)*
* **Visuals:** Logic gate animations showing multi-criteria document filtering.
* **The Code Sandbox:**
  ```javascript
  db.products.find({
    $and: [
      { category: { $in: ["Electronics", "Computers"] } },
      { price: { $gte: 100, $lte: 999 } },
      { tags: { $all: ["wireless", "gaming"] } } // Must have BOTH tags
    ]
  });
  ```

---

## 🗄️ 06:00 PM — SQL Masterclass (Episode 3)
* **Title:** *The Aggregation Engine: `GROUP BY`, `HAVING`, `SUM`, `AVG`, `COUNT`*
* **Visuals:** Bucket-sorting animation. Rows dropping into department bins and collapsing into scalar revenue totals.
* **The Code Sandbox:**
  ```sql
  SELECT department_id, COUNT(*) AS total_staff, AVG(salary) AS avg_sal
  FROM employees
  WHERE status = 'Active'
  GROUP BY department_id
  HAVING AVG(salary) > 75000;
  ```
* **Anti-Pattern:** Putting aggregate calculations in `WHERE` (`WHERE AVG(salary) > 75000` is illegal syntax!).

---
---

# 📅 DAY 4: Functions, Scopes, Atomic Updates & Joins

---

## 🐍 10:00 AM — Python Masterclass (Episode 4)
* **Title:** *Mastering Functions: Scopes (`LEGB`), Closures, `*args` & `**kwargs`*
* **Visuals:** Nested transparent scope boxes: **L**ocal $\rightarrow$ **E**nclosing $\rightarrow$ **G**lobal $\rightarrow$ **B**uilt-in.
* **The Code Sandbox:**
  ```python
  def make_multiplier(factor):
      def multiply(number):
          return number * factor  # Remembers 'factor' from enclosing scope (Closure!)
      return multiply

  double = make_multiplier(2)
  print(double(5))  # 10
  ```

---

## ☕ 12:00 PM — Java Masterclass (Episode 4)
* **Title:** *Methods Deep Dive: Pass-by-Value Proof, Overloading & Variable Arguments*
* **Visuals:** Stack frame simulator proving that Java passes the *value* of the pointer, never the pointer itself.
* **The Code Sandbox:**
  ```java
  public static void swap(int a, int b) {
      int temp = a;
      a = b;
      b = temp; // Has ZERO effect on variables in main()!
  }
  ```

---

## 🍃 02:00 PM — MongoDB Masterclass (Episode 4)
* **Title:** *Atomic Document Updates: `$set`, `$inc`, `$push`, `$addToSet` & `upsert`*
* **Visuals:** In-place disk update animation modifying a single key without rewriting the document.
* **The Code Sandbox:**
  ```javascript
  db.users.updateOne(
    { email: "alex@example.com" },
    {
      $inc: { login_count: 1 },
      $set: { last_login: new Date() },
      $addToSet: { ip_history: "192.168.1.1" } // Prevents duplicates!
    },
    { upsert: true } // Creates document if it doesn't exist!
  );
  ```

---

## 🗄️ 06:00 PM — SQL Masterclass (Episode 4)
* **Title:** *The Power of `JOINs`: `INNER JOIN` vs `LEFT JOIN` Demystified*
* **Visuals:** Side-by-side table connection lines showing matching foreign keys.
* **The Code Sandbox:**
  ```sql
  -- Find customers who have NEVER placed an order
  SELECT c.customer_name, c.email
  FROM customers c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
  WHERE o.order_id IS NULL;
  ```

---
---

# 📅 DAY 5: Object-Oriented Programming & Advanced Relationships

---

## 🐍 10:00 AM — Python Masterclass (Episode 5)
* **Title:** *OOP in Python: Classes, Instances, `__init__`, and What `self` Actually Means*
* **Visuals:** Factory blueprint stamping out isolated instance objects in Heap memory.
* **The Code Sandbox:**
  ```python
  class BankAccount:
      def __init__(self, owner, balance=0.0):
          self.owner = owner
          self._balance = balance  # Protected attribute

      def deposit(self, amount):
          if amount > 0:
              self._balance += amount
              return True
          return False
  ```
* **Anti-Pattern:** Defining mutable class-level attributes (`class Dog: tricks = []`) where all dog instances share the exact same tricks list!

---

## ☕ 12:00 PM — Java Masterclass (Episode 5)
* **Title:** *Encapsulation & Constructors: Data Hiding, Getters/Setters & Constructor Chaining*
* **Visuals:** A bank vault object: outside classes must authenticate through public methods rather than directly tampering with private fields.
* **The Code Sandbox:**
  ```java
  public class Employee {
      private String name;
      private double salary;

      public Employee(String name) {
          this(name, 50000.0); // Constructor chaining using this()
      }

      public Employee(String name, double salary) {
          this.name = name;
          this.salary = salary;
      }
  }
  ```

---

## 🍃 02:00 PM — MongoDB Masterclass (Episode 5)
* **Title:** *Schema Design Architecture: When to Embed vs When to Reference*
* **Visuals:** Architecture comparison: Single nested document with embedded sub-documents vs separate linked collections using `$lookup`.
* **The 3 Golden Rules:**
  1. **Embed** if 1-to-Few (e.g., a user having 2 addresses).
  2. **Reference** if 1-to-Many (e.g., a product having 50,000 reviews).
  3. **Parent Reference** if 1-to-Squillions (e.g., sensor log events referencing server ID).

---

## 🗄️ 06:00 PM — SQL Masterclass (Episode 5)
* **Title:** *Advanced `JOINs`: `RIGHT`, `FULL OUTER`, `CROSS` & The Genius of Self Joins*
* **Visuals:** Animated hierarchy tree showing an Employee table joining back onto itself to pair employees with their managers.
* **The Code Sandbox:**
  ```sql
  -- Self Join: Find employees who earn more than their direct manager
  SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
  FROM employees e
  JOIN employees m ON e.manager_id = m.employee_id
  WHERE e.salary > m.salary;
  ```
