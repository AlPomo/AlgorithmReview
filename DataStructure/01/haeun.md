# Array와 List

## 📚특징

### Array

* 같은 자료형의 집합을 의미함
* 배열의 길이가 고정되어 있음
* 연속된 메모리 공간으로 이뤄져있음

### ArrayList

* [Dynamic Array](https://en.wikipedia.org/wiki/Dynamic_array)

* 연속적으로 데이터를 묶어 저장한다.

* 인덱스로 무작위 접근이 가능하다.

* 복잡도

  * 검색 O(1)

  * 삽입/삭제 O(N)

    사이즈를 늘리고, 삽입/삭제 위치 기준으로 기존 데이터들이 앞 뒤로 이동하기 때문. 또한 삭제될 때, 메모리 낭비가 발생함

### LinkedList

* 무한개의 자료 삽입 가능함
* 복잡도
  * 검색 O(N) : 인덱스가 없으므로 순차접근하여 검색에 불리함
  * 삽입/삭제 O(1)



## 📚장단점

|            | 장점                                                         | 단점                                                      |
| ---------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| Array      | 인덱스 검색이 용이함, 연속적이므로 메모리 관리가 편함        | 메모리 낭비가 심함, 배열 크기 변동 불가                   |
| ArrayList  | 내부 데이터를 배열에서 관리하기 때문에, 인덱스를 이용한 데이터 접근이 용이해 **검색**성능이 좋음 | 배열 이용한 연산으로 삽입/삭제 시 메모리 낭비             |
| LinkedList | 노드 간 연결로 **삽입/삭제** 성능이 좋음                     | 검색 시 모든 요소를 탐색하기 때문에, 검색성능이 좋지 않음 |



## 📚Java API

### ArrayList

```java
import java.util.List;
import java.util.ArrayList;

	public static void main(String[] args) {
		//선언
        List<Integer> list = new ArrayList<>();
        List<Integer> list = new LinkedList<>();
		
		/*
		 * (1) 추가
		 * list.add(element): 단순히 배열 뒤에 데이터를 더하기 때문에 빠르다.
		 * list.add(idx, element): 배열 연산이므로, idx 접근이 가능하다.
		 * 
		 * 내부 배열의 크기가 한계에 도달했을 때, 기존배열의 2배 긴 배열을 만들어 복제하므로
		 * 개발자는 크기를 신경쓰지 않아도 된다는 장점이 있다.
		 */
		
        /*
		 * (2) 삭제
		 * list.remove(idx): 인덱스에 해당하는 요소를 찾아 삭제
		 * list.remove(object): 리스트에서 object와 동일한 요소를 찾아 삭제
		 * list.removeAll(list2): list에서 list2의 동일 요소를 모두 찾아 삭제
		 */
		
		/*
		 * (3) 가져오기
		 * list.get(idx): 인덱스에 해당하는 요소를 검색
		 */
		
		/*
		 * (4) 반복
		 * Iterator<Integer> it = list.iterator();
		 * while(it.hasNext()) {
		 *		System.out.println(it.next());
		 * }
		 * 
		 * for문은 집합의 전체 크기를 알아야 하지만, Iterator의 경우 크기를 몰라도 가능함
		 */
        
	}
```



## 📚구현

### ArrayList

```java
public class ArrayList_Implementation {
	private static final int INIT_SIZE = 10;
	static class ArrayList {
		private int size = 0;
		private Object[] elementData = new Object[INIT_SIZE];
		
		private void expandArray() {
			Object[] newArray = new Object[size*2];
			for(int i=0; i<elementData.length; i++) {
				newArray[i] = elementData[i];
			}
			elementData = newArray;
		}
		
		public boolean addLast(Object element) {
			if(elementData.length==size) expandArray();
			elementData[size++] = element;
			return true;
		}
		
		public boolean add(int idx, Object element) {
			if(elementData.length==size) expandArray();
			for(int i=size-1; i>=idx; i--) {
				elementData[i+1] = elementData[i]; 
			}
			elementData[idx] = element;
			size++;
			return true;
		}
		
		public boolean addFirst(Object element) {
			return add(0, element);
		}
		
		public Object remove(int idx) {
			Object removed = elementData[idx];			
			for(int i=idx+1; i<=size-1; i++) {
				elementData[i-1] = elementData[i];
			}
			elementData[size--] = null;
			return removed;
		}
		
		public Object removeFirst() {
			return remove(0);
		}
		
		public Object removeLast() {
			return remove(size-1);
		}
		
		public Object get(int idx) {
			return elementData[idx];
		}
		
		@Override
		public String toString() {
			StringBuilder sb = new StringBuilder();
			sb.append("ArrayList = [");
			for(int i=0; i<size; i++) {
				sb.append(elementData[i]);
				if(i<size-1) sb.append(",");
			}
			return sb.append("]").toString();
		}
		
	}
	
	public static void main(String[] args) {
		ArrayList arrayList = new ArrayList();
		arrayList.addLast(10);
		arrayList.addLast(20);
		arrayList.addLast(30);
		arrayList.addLast(40);
		arrayList.addLast(10);
		arrayList.addLast(20);
		arrayList.addLast(30);
		arrayList.addLast(40);
		arrayList.addLast(10);
		arrayList.addLast(20);
		arrayList.add(2, 2000);
		System.out.println(arrayList.toString());
		
		arrayList.remove(6);
		arrayList.removeFirst();
		arrayList.removeLast();
		System.out.println(arrayList.toString());
		
		arrayList.get(0);
		System.out.println(arrayList.get(1));
	}
}

```



### LinkedList

```java
public class LinkedList_Implementation {
	private static class Node {
		private Object data;
		private Node next; //다음 노드를 가르킨다.
		
		public Node(Object input) {
			this.data = input;
			this.next = null;
		}
		
		@Override
		public String toString(){
            return String.valueOf(this.data);
        }
	}
	static class LinkedList {		
		private Node head;
		private Node tail;
		private int size = 0;
		
		@Override
		public String toString() {
			if(head == null) return "[]";
			StringBuilder sb = new StringBuilder();
			sb.append("[");
			Node tmp = head;
			while(tmp.next!=null) {
				sb.append(tmp.data).append(",");
				tmp = tmp.next;
			}
			sb.append(tmp.data).append("]");
			return sb.toString();
		}
		
		public int size() {
			return size;
		}
		
		public void addFirst(Object input) {
			Node newNode = new Node(input);
			newNode.next = head;
			head = newNode;
			size ++;
			if(head.next==null) tail=head;
		}
		
		private Node node(int idx) {
			Node x = head;
			for(int i=0; i<idx; i++) {
				x = x.next;
			}
			return x;
		}
		
		public void add(int idx, Object input) {
			Node newNode = new Node(input);
			
			if(size==0 || idx==0) {
				addFirst(input);
			} else {
				Node pre = node(idx-1);
				Node next = node(idx);
				pre.next = newNode;
				newNode.next = next;				
				size++;
				
				if(newNode.next==null) {
					tail = newNode;
				}
			}
		}
		
		public void addLast(Object input) {
			Node newNode = new Node(input);
			if(size==0) {
				addFirst(input);
			} else {
				tail.next = newNode;
				tail = newNode;
				size++;
			}
		}
		
		public void removeFirst() {
			Node origin_head = head;
	        head = head.next;
	        origin_head = null;
	        size--;
		}
		
		public void remove(int idx) {
			if(idx==0) removeFirst();
			
			Node pre = node(idx-1);
			Node removed = pre.next;
			pre.next = pre.next.next;
			
			//만약 삭제하려는 데이터가 tail이었다면
			if(removed==tail) {
				tail = pre;
			}
			
			removed = null;
			size --;
		}
		
		public void removeLast() {
			remove(size-1);
		}
		
		public Object get(int idx) {
			return node(idx);
		}
	}
	public static void main(String[] args) {
		LinkedList linkedlist = new LinkedList();
		linkedlist.addFirst(1);
		System.out.println(linkedlist);
		
		linkedlist.add(0, 0);
		linkedlist.addLast(100);
		linkedlist.add(2, 2);
		linkedlist.addLast(200);
		System.out.println(linkedlist);
		
		linkedlist.removeFirst();
		System.out.println(linkedlist);
		
		//linkedlist.remove(3);
		//linkedlist.remove(1);
		linkedlist.removeLast();
		System.out.println(linkedlist);
		
		linkedlist.get(2);
		System.out.println(linkedlist.get(1));
	}
}

```



## 📚Collections.sort() java 8

[참고](https://m.blog.naver.com/PostView.nhn?blogId=pistolcaffe&logNo=221020950346&proxyReferer=https:%2F%2Fwww.google.com%2F)

(1) Collection.sort() → TimSort.sort()

```java
import java.util.*;

public class Array {
	public static void main(String[] args) {
		List<Integer> list = new LinkedList<>();

		/*
		 * TimSort 상황에 따라 binary search를 이용한 삽입정렬과 병합정렬이 적절히 사용됨
		 * 최악의 경우에도 o(nlogn)을 보장함
		 */
		Collections.sort(list);

	}

	public static <T extends Comparable<? super T>> void sort(List<T> list) {
		list.sort((Comparator) null);
	}

	public static void sort(Comparator<? super E> c) {
		Object[] a = this.toArray();
		Arrays.sort(a, c);
		ListIterator<E> i = this.listIterator();
		Object[] var4 = a;
		int var5 = a.length;

		for (int var6 = 0; var6 < var5; ++var6) {
			Object e = var4[var6];
			i.next();
			i.set(e);
		}

	}

	public static <T> void sort(T[] a, Comparator<? super T> c) {
		if (c == null) {
			sort(a);
		} else if (Arrays.LegacyMergeSort.userRequested) {
			legacyMergeSort(a, c);
		} else {
			TimSort.sort(a, 0, a.length, c, (Object[]) null, 0, 0);
		}
	}
	
	/** 실제로 MergeSort는 사용하지 않도록 구현되어 있다. */
	static final class Lega Never use circular merge sort.
		private static final boolean userRequested = false;
	}
	
}

```



(2) Timsort 초기분기

```java
if (nRemaining < MIN_MERGE) { //JAVA기준 MIN_MERGE = 32
    PistolLogger.LOGE("do binarySort()");
    int initRunLen = countRunAndMakeAscending(a, lo, hi, c);
    binarySort(a, lo, hi, lo + initRunLen, c);
    return;
}
```

nRemaining(내가 정렬할 자료크기) 크기 값이 MIN_MERGE 이하면, 삽입정렬

 

(2) run과 minrun

run은 정렬할 배열을 나누는 것으로, 이 최소 값인 minrun 길이를 계산해야 한다. run으로 나눠진 내부에서는 삽입정렬이 일어나기 때문에 너무 커도 안되며, 너무 짧아도 병합(Merge)시 복잡하기 때문에 적절한 값을 내는 것이 중요하다.

```java
int minRun = minRunLength(nRemaining);

private static int minRunLength(int n) {
    assert n >= 0;
    int r = 0; // Becomes 1 if any 1 bits are shifted off
    while (n >= MIN_MERGE) {
        r |= (n & 1);
        n >>= 1;
    }
    return n + r;
}
```



(3) countRunAndMakeAscending

```java
do {
    // Identify next run
    int runLen = countRunAndMakeAscending(a, lo, hi, c);

    // If run is short, extend to min(minRun, nRemaining)
    if (runLen < minRun) {
        int force = nRemaining <= minRun ? nRemaining : minRun;
        binarySort(a, lo, lo + force, lo + runLen, c);
        runLen = force;
     }
    ....
} while (nRemaining != 0);

private static <T> int countRunAndMakeAscending(T[] a, int lo, int hi,
                                            Comparator<? super T> c) {
    assert lo < hi;
    int runHi = lo + 1;
    if (runHi == hi)
        return 1;

    // Find end of run, and reverse range if descending
    if (c.compare(a[runHi++], a[lo]) < 0) { // Descending
        while (runHi < hi && c.compare(a[runHi], a[runHi - 1]) < 0)
            runHi++;
        reverseRange(a, lo, runHi);
    } else {                              // Ascending
        while (runHi < hi && c.compare(a[runHi], a[runHi - 1]) >= 0)
            runHi++;
    }

    return runHi - lo;
}
```



(4) binarySort()

```java
// If run is short, extend to min(minRun, nRemaining)
if (runLen < minRun) {
    int force = nRemaining <= minRun ? nRemaining : minRun;
    binarySort(a, lo, lo + force, lo + runLen, c);
    runLen = force;
}
```

나눠진 run을 기준으로 binarySort()를 통해 삽입정렬을 수행한다.



(5) merge

```java
...
// Push run onto pending-run stack, and maybe merge
ts.pushRun(lo, runLen);
ts.mergeCollapse();
...

private void pushRun(int runBase, int runLen) {
    this.runBase[stackSize] = runBase;
    this.runLen[stackSize] = runLen;
    stackSize++;
}
```

인접한 run끼리 병합되며, 순서가 뒤바뀌지 않도록 두개의 쌍 stack이 활용됨
