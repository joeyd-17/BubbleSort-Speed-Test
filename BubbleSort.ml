(*Take in the size from the command line*)
let size =
  if Array.length Sys.argv > 1 then int_of_string Sys.argv.(1) else 1000;;

Printf.printf "Looking for size: %d\n" size;;

(*Create a custom int list type*)
type intList = Nil | Cons of (int * intList)

exception EmptyList
exception OutOfBounds

(*Function to read the first n lines in from file*)
let rec readIn f n = 
  if n > 0 then
    try
      let line = int_of_string (input_line f) in
        Cons(line, readIn f (n - 1))

    with
    | End_of_file -> Nil

  else Nil

(*Removes the first n items in the int list*)
(*Helper function for concatIntList*)
let rec removeStart n l =
  if n = 0 then l else
    match l with
    | Nil -> raise OutOfBounds
    | Cons(x, Nil) -> Nil
    | Cons(x, xs) -> removeStart (n - 1) xs
    
(*Removes the last n items in the int list*)
(*Helper function for concatIntList*)
let rec removeEnd n l =
  if n = 0 then Nil else
    match l with
    | Nil -> raise OutOfBounds
    | Cons(x, Nil) -> Cons(x, Nil)
    | Cons(x, xs) -> Cons(x, removeEnd (n - 1) xs)

(*Function to concatinate an int list*)
let concatIntList x y l =
  if x <= y then
    let shortList = removeStart x l in
      removeEnd y shortList
  else
    (*if y < x then flip the order*)
    let shortList = removeStart y l in
      removeEnd x shortList

(*Get the size of a int list*)
let rec intListSize l =
  match l with
  | Nil -> 0
  | Cons(x, Nil) -> 1
  | Cons(x, xs) -> 1 + intListSize xs

(*Function to print int list*)
let rec printIntList l =
  match l with
  | Nil -> "Empty List!"
  | Cons(x, Nil) -> string_of_int x
  | Cons(x, xs) -> (string_of_int x) ^ ", " ^ (printIntList xs)

(*Index into an int list*)
let index i l =
  let list = concatIntList i i l in
    match list with
    | Nil -> raise EmptyList
    | Cons(x, Nil) -> x
    | Cons(x, xs) -> x

(*Check if two int lists are equal*)
let rec isEq a b =
  match (a, b) with
  | (Nil, Nil) -> true
  | (x, Nil) -> false
  | (Nil, y) -> false
  | (Cons(x, xs), Cons(y, ys)) -> 
    if x = y then isEq xs ys else false

(*Bubble Sort the int list*)
let rec bubbleSortStep l =
  match l with
  | Nil -> raise EmptyList
  | Cons(x, Nil) -> (Cons(x, Nil))
  | Cons(x, Cons(y, xs)) -> if x > y 
    then Cons(y, bubbleSortStep (Cons(x, xs)))
    else Cons(x, bubbleSortStep (Cons(y, xs)))

let rec bubbleSort l =
  let step = bubbleSortStep l in
    if isEq l step then l else bubbleSort step

(*Read in from file into numbers array*)
let numbers = 
  let file = open_in "numbers.txt" in
    readIn file size;;

Printf.printf "Size of intList: %d\n" (intListSize numbers)

let sortedNumbers = bubbleSort numbers;;
Printf.printf "First and last 10: %s...%s" (printIntList (concatIntList 0 10 sortedNumbers)) (printIntList (concatIntList (intListSize sortedNumbers - 10) size sortedNumbers))