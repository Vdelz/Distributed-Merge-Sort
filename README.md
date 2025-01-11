# External MergeSort in Python

  Implemented *Pythonic* way as well as *low level native External Merge Sort*
  
  **Problem Stement** </br>
  All Sorting Algorithm works within the RAM. When the data to be sorted does not fit into the RAM
  but in the slower external memory (usually a hard drive), this technique is used.
  [external merge sort](https://en.wikipedia.org/wiki/External_sorting)

**How to ?**

> Split Phase
* Split the dataset into chunks each one smaller than the RAM
* Sort the rows inside each chunk using some efficient Sorting Algo in O(n log(n))
* Stores each of the sorted small chunks to disk.

> Merge Phase
* Do a [K-way merge](https://en.wikipedia.org/wiki/K-way_merge_algorithm) of the chunks.

Inline the details.
* After the Split Phase, A list of file handlers of all the chunks will be stored - **sortedTempFileHandlerList**
* We create a list of heap-nodes - **heapnodes**. Each heap-node will store the actual entry read from each chunk and also the file which owns it. 
   - Loop While Least Element (the top of heap ) is **INT_MAX**
     * Picks the node with min element from heap-nodes.
     * Write the element to  **sortedLargeFile** (it will be the sorted number)
     * Find the *filehandler* of the corresponding element by looking at heapnode.filehandler.
     * Read the next item from the file. If it's **EOF**, mark the item as **INT_MAX**  
     * Put the item at the heap-top.
     * Heapify to persist min-heap property.
      
* At the end of the Merge Phase **sortedLargeFile** will have all the elements in sorted order.
