import scala.annotation.tailrec

object Hello extends App {
  import Fib.{fib, fibTail}
  for (i <- 0 to 10) {
    println(fib(i))
  }
}

object Fib {
  def fib(n: Int): Int = fibTail(n, 0, 1)
  @tailrec
  def fibTail(n: Int, prev: Int, acc: Int): Int = {
    if (n <= 1) acc else fibTail(n - 1, acc, acc + prev)
  }
}
