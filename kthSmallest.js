// Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

const TreeNode = function(val) {
  this.val = val;
  this.left = null;
  this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
const kthSmallestNaive = (root, k) => {
  // Build array from contents of BST using in order traversal
  const traversal = [];
  // Helper function to perform in order traversal
  // will build a sorted array with contents of bst in traversal
  const traverse = (node) => {
    if (node.left) {
      traverse(node.left);
    }
    traversal.push(node.val);
    if (node.right) {
      traverse(node.right);
    }
  }
  traverse(root);
  return traversal[k-1];
}
//Does not require storing entire tree contents if tree is very large
const kthSmallest = (root, k) => {
  let count = 0;
  let stack = [];
  while (count < k) {
    if (root) {
      stack.push(root);
      root = root.left;
    } else {
      if (stack) {
        root = stack.pop();
        count++;
        if (count === k) {
          break
        }
        root = root.right;
      } else {
        break;
      }
    }
  }
  return root.val;
}

const test = () => {
  let root = new TreeNode(3);
  let branch1 = new TreeNode(1);
  root.left = branch1;
  let leaf1 = new TreeNode(2);
  branch1.right = leaf1;
  let branch2 = new TreeNode(4);
  root.right = branch2;
  console.log(kthSmallest(root, 1));

}
test();