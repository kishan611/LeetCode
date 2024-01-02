class MinStack {
    private class Node{
        int x;
        int min;
        Node next;
        private Node(int x,int min,Node next){
            this.x=x;
            this.min=min;
            this.next=next;
        }
        
    }
    private Node head;
    
    public void push(int val) {
        if(head==null){
            head=new Node(val,val,null);
        }
        else{
            head=new Node(val,Math.min(val,head.min),head);
        }
    }
    
    public void pop() {
        head=head.next;
    }
    
    public int top() {
        return head.x;
    }
    
    public int getMin() {
        return head.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */