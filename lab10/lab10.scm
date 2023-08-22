(define (make-adder num) 
(lambda (inc) (+ inc num))
)



(define (composed f g ) 
  (lambda (x) (f (g x) )) 
)



(define (my-filter pred s) 

(cond ((null? s) nil )
((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
(else  (my-filter pred (cdr s))))

)
;;;cond applies to (pred s)     





(define (exp b n)
  (define (helper b n so-far) 
    (if ( = n 0)
    so-far
    (helper b (- n 1) (* b so-far))
    )
  )
  (helper b n 1))


(define (interleave lst1 lst2 ) 

  (if (or (null? lst1) (null? lst2))
  (append lst1 lst2)
  (cons (car lst1) (cons (car lst2)(interleave (cdr lst1)(cdr lst2)))))
  
)


(define (square n) (* n n))



(define (pow base exp) 
(cond ((= exp 0) 1)
((even? exp) (square (pow base (/ exp 2))))
(else (* base (pow base (- exp 1))))

)
)
