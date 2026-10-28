class Container:
        class Package:
            def __init__(self,owner,weight,iden = 0,next_package = None): 
                '''
                purpose: initialize a package object with owner name, weight, identifier, and next pointer
                parameters: 
                    owner: string representing the owner of the package
                    weight: numeric value representing the weight of the package
                    iden: integer identifier for the package (defaults to 0)
                    next_package: reference to the next package node in the linked list (defaults to None)
                throws: none
                pre: owner must be a string and weight must be a valid numeric value
                post: package is initialized with the specified attributes and next link
                returns: none
                '''
                self._owner = owner
                self._weight = weight
                self._iden = iden
                self._next_package = next_package
            

            def __str__(self):
                '''
                purpose: return a formatted string representation of the package containing its iden, owner, and weight
                parameters: none
                throws: none
                pre: package instance must be properly initialized with valid attribute values
                post: string representation is generated and returned without modifying the package state
                returns: string containing the formatted package details
                '''
                return f'{self._iden}: {self._owner}, {self._weight}'

            def __repr__(self):
                '''
                purpose: return a string representation of the package
                parameters: none
                throws: none
                pre: package is initialized
                post: package is unmodified
                returns: formatted string with iden, owner, and weight
                '''
                return str(self)

            def set_owner(self , new_owner):
                '''
                purpose: update the owner of the package
                parameters: new_owner: string representing the new owner
                throws: none
                pre: new_owner is a valid string
                post: package owner attribute is updated
                returns: none
                '''
                self._owner = new_owner

            def set_weight(self, new_weight):
                '''
                purpose: update the weight of the package
                parameters: new_weight: numeric value representing the new weight
                throws: none
                pre: new_weight is a valid number
                post: package weight attribute is updated
                returns: none
                '''
                self._weight = new_weight

            def set_id(self,id):
                '''
                purpose: update the package identifier
                parameters: id: integer representing the new identifier
                throws: none
                pre: id is a valid integer
                post: package identifier attribute is updated
                returns: none
                '''
                self._iden = id

            def get_next(self):
                '''
                purpose: return the reference to the next package in the list
                parameters: none
                throws: none
                pre: package is initialized
                post: package is unmodified
                returns: reference to the next package node or None
                '''
                return self._next_package

            def __eq__(self,other):
                '''
                purpose: check if two packages are equal based on their identifiers
                parameters: other: object being compared to this package
                throws: none
                pre: none
                post: packages are unmodified
                returns: True if other is a package with the same identifier, False otherwise
                '''
                if  isinstance(other , Container.Package):
                    return self._iden == other._iden
                else:
                    return False

            def owner(self):
                '''
                purpose: return the owner of the package
                parameters: none
                throws: none
                pre: package is initialized
                post: package is unmodified
                returns: string representing the package owner
                '''
                return self._owner

            def weight(self):
                '''
                purpose: return the weight of the package
                parameters: none
                throws: none
                pre: package is initialized
                post: package is unmodified
                returns: numeric value representing the package weight
                '''
                return self._weight
            
            def package_id(self):
                '''
                purpose: return the identifier of the package
                parameters: none
                throws: none
                pre: package is initialized
                post: package is unmodified
                returns: integer representing the package identifier
                '''
                return self._iden
            
            def set_next(self, new_next):
                '''
                purpose: update the reference to the next package
                parameters: new_next: reference to the next package node or None
                throws: none
                pre: none
                post: next package pointer attribute is updated
                returns: none
                '''
                self._next_package = new_next

            

        def __init__(self): 
            '''
            purpose: initialize an empty container for packages
            parameters: none
            throws: none
            pre: none
            post: container is initialized with zero elements, zero total weight, and starting id set to 1
            returns: none
            '''
            self.front = None
            self.size = 0
            self.total_weight = 0
            self.next_id = 1

        def isEmpty(self):
                '''
                purpose: check if the container is empty
                parameters: none
                throws: none
                pre: none
                post: container is unmodified
                returns: True if container has no packages, False otherwise
                '''
                if self.size == 0:
                    return True
                else:
                    return False
  
        def add_package(self, p): 
            '''
            purpose: insert a new package into the container in sorted order based on owner and weight
            parameters: p: package object to add
            throws: none
            pre: p is a valid Package instance
            post: package is added in sorted position, container size, total weight, and next_id are updated
            returns: none
            '''
            if self.isEmpty() == True:
             p.set_id(self.next_id) 
             
             self.front = p 
             self.size += 1
             self.total_weight += p.weight()
             self.next_id += 1
             return

            
            if ( p.owner() < self.front.owner() or 
                p.owner() == self.front.owner() and p.weight() > self.front.weight()):
                p.set_next(self.front)
                p.set_id(self.next_id) #this is initialized to 1
                self.front = p
                self.size += 1
                self.total_weight += p.weight()
                self.next_id += 1

                return
            

          

            prev_node = self.front
            curr_node = prev_node.get_next()
            while curr_node != None and curr_node.owner() < p.owner():
                prev_node = curr_node
                curr_node = curr_node.get_next()

            while curr_node != None and curr_node.owner() == p.owner() and curr_node.weight() > p.weight():
                prev_node = curr_node
                curr_node = curr_node.get_next()
                

            p.set_next(curr_node) 
            prev_node.set_next(p) 
            p.set_id(self.next_id)
            self.size += 1
            self.total_weight += p.weight()
            self.next_id += 1

            return

            
        def __str__(self):
            '''
            purpose: return a string representation of all packages in the container
            parameters: none
            throws: none
            pre: container is initialized
            post: container is unmodified
            returns: formatted string containing all packages
            '''
            string = ''
            curr_node = self.front
            while curr_node != None:
                string += f'{str(curr_node)}, ' 
                curr_node = curr_node.get_next()
            return string
  
        def is_empty(self):
            '''
            purpose: check if the container is empty
            parameters: none
            throws: none
            pre: none
            post: container is unmodified
            returns: True if the container has no packages, False otherwise
            '''
            if self.front == None:
                return True
            else:
                return False

        def get_weight(self):
                '''
                purpose: return the total weight of all packages in the container
                parameters: none
                throws: none
                pre: container is initialized
                post: container is unmodified
                returns: numeric value representing the total weight
                '''
                return self.total_weight 

        def get_first(self):
            '''
            purpose: return the reference to the first package in the container
            parameters: none
            throws: none
            pre: container is initialized
            post: container is unmodified
            returns: reference to the first package node or None
            '''
            return self.front

        def get_num_packages(self):
            '''
            purpose: return the total number of packages currently in the container
            parameters: none
            throws: none
            pre: container is initialized
            post: container is unmodified
            returns: integer representing the number of packages
            '''
            return self.size


        def search_package_by_id(self, id):
            '''
            purpose: search for a package by its identifier and print it if found
            parameters: id: integer representing the package identifier
            throws: none
            pre: container is initialized
            post: container is unmodified
            returns: True if the package is found, False otherwise
            '''
            curr_node = self.front
            if id == curr_node._iden :
                print(curr_node)
                return True
            else:
                tmpRef = self.front
                if tmpRef == None :
                    return False
                
                if (id == 0) or id > self.size:
                    print('There are no packages with that ID')
                    return False
                
                while tmpRef != None :
                    if tmpRef._iden == id:
                        print(tmpRef)
                        return True
                    tmpRef = tmpRef.get_next()

        def show_packages_by_owner(self,name):
            curr_node = self.front
            found = False
            while curr_node != None :
                if name == curr_node.owner():
                    print(curr_node)
                    found = True
                curr_node = curr_node.get_next()

            if found == False:
                print('There are no packages with that name')
            return found

        def show_packages_by_weight(self,weight):
            '''
            purpose: return the total weight of all packages in the container
            parameters: none
            throws: none
            pre: container is initialized
            post: container is unmodified
            returns: numeric value representing the total weight
            '''
            curr_node = self.front
            found = False
            while curr_node != None :
                if weight == curr_node.weight():
                    print(curr_node)
                    found = True
                curr_node = curr_node.get_next()
            
            if found == False:
                print('There are no packages with that weight')
            return found
            
        def remove_packages_by_weight(self,weight):
            '''
            purpose: remove a package matching the specified weight from the container
            parameters: weight: numeric value representing the weight to remove
            throws: none
            pre: container is initialized
            post: matching package is removed if present, container size and links are updated
            returns: True if a package is removed, False otherwise
            '''
            if self.isEmpty():
                return

            if weight == self.front.weight():
                self._size -= 1
                self._front = self._front._get_next()
                return True

            tmpRef = self.front
            while tmpRef.get_next() != None and weight > tmpRef._get_next._weight():
                tmpRef = tmpRef.get_next()

            if tmpRef.get_next() == None:
                print('There is no package with that weight')
                return False
            if tmpRef.get_next().weight() != weight:
                return False
            self._size -= 1
            tmpRef.set_next(tmpRef.get_next().get_next()) 
            return True

        def remove_packages_by_owner(self,name):
            '''
            purpose: remove a package matching the specified owner name from the container
            parameters: name: string representing the owner name to remove
            throws: none
            pre: container is initialized
            post: matching package is removed if present, container size and links are updated
            returns: True if a package is removed, False otherwise
            '''
            if self.isEmpty():
                return
            
                       
            if name == self.front.owner():
                 self._size -= 1
                 self._front = self._front._get_next()
                 return True
            
            tmpRef = self.front
            while tmpRef.get_next() != None and name > tmpRef._get_next._owner():
                tmpRef = tmpRef.get_next()
            
            if tmpRef.get_next() == None:
                print('There is no package with that name')
                return False
            if tmpRef.get_next().owner() != name:
                    return False
            self._size -= 1
            tmpRef.set_next(tmpRef.get_next().get_next()) 
            return True
            


####TESTING PACKAGE INIT########
#p1 = Package('Cisco', 5 )
#p2 = Package('Cisco', 5, 1)
#print(p1.package_id())
#print(p1.get_next())
#print(p1.weight())
#print(p1.owner())
#print(p2.package_id())
#print(p2.get_next())

####TESTING PACKAGE SETTERS ########
#p = Package('Cisco',5, 1 )
#p.set_weight(50)
#print(p.weight())
#p.set_owner('NEW')
#print(p.owner())
#p.set_id(4)
#print(p.package_id())
#p3 = Package('NEW',5,1,p)
#print(p3.get_next())

#TESTING PACKAGE EQ
#p = Package('Cisco', 5, 1)
#p1 = Package('Cisco', 15, 1)
#p2 = Package('Cisc', 5, 12)
#p3 = Package('Apple', 5, 10)
#p4 = Package('Cisco', 5, 1)
#p5 = Package('Cisc', 50, 10)
#print(p == p1)
#print(p == p2)
#print(p == p3)
#print(p == p4 )
#print(p == p5)

##TEST ADDING ONE PACKAGE
#c = Container() #ask again how that add package bit worked
#p = Container.Package('Cisco',25)
#c.add_package(p)
#print(c.get_num_packages())
#print(c.get_weight())
#print(p.package_id())
#print(c.is_empty())


#print(c.front.get_next())

#c.add_package(Container.Package('Amazon', 35))
#print(c)
#c.add_package(Container.Package('Dunkin Donuts', 35))
#c.add_package(Container.Package('Dunkin Donuts', 45))
#print(c)


##TEST ADDING PACKAGE CORRECT ORDER
#c = Container()
#p1 = Container.Package('Apple',3)
##p2 = Container.Package('Cisco', 8)
#p3 = Container.Package('Zen', 10)
#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#p = c.get_first()
#print(p.get_next())
##print(p.get_next().get_next())
#print(c.get_num_packages())
#print(c.get_weight())
#print(p1.package_id())
#print(p2.package_id())
#print(p3.package_id())

##TEST ADDING PACKAGE INCORRECT ORDER
#c = Container()
#p1 = Container.Package('Zen',3)
#p2 = Container.Package('Apple',3)
#p3 = Container.Package('Cisco', 10)
#p4 = Container.Package('Apple',8)
#p5 = Container.Package('Cisco',3)
#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#c.add_package(p4)
#c.add_package(p5)
#p = c.get_first()
#print(p)
#print(p.get_next())
#print(p.get_next().get_next())
#print(p.get_next().get_next().get_next())
#print(p.get_next().get_next().get_next().get_next())
#print(c.get_num_packages())
#print(c.get_weight())

##TEST ADDING PACKAGE DOUBLE TIE
#c = Container()
#p1 = Container.Package('Apple', 3)
#p2 = Container.Package('Apple', 3)
#p3 = Container.Package('Apple', 8)
#p4 = Container.Package('Apple', 8)
#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#c.add_package(p4)
#p = c.get_first()
#print(p)
#print(p.get_next())
#print(p.get_next().get_next())
#print(p.get_next().get_next().get_next())
#print(p1.package_id())
#print(p2.package_id())
#print((p3.package_id()))
#print(p4.package_id())

##TEST PACKAGE SEARCH PACKAGE BY ID
#c = Container()
#p1 = Container.Package('Apple', 3)
#p2 = Container.Package('Apple', 4)
#p3 = Container.Package('Cisco', 8)
#p4 = Container.Package('Cisco', 8)

#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#c.add_package(p4)

#print(c.search_package_by_id(1))  
#print((c.search_package_by_id(2))) 
#print(c.search_package_by_id(3))
#print((c.search_package_by_id(4)))

#print((c.search_package_by_id(0)))
#print((c.search_package_by_id(5)))
#print((c.search_package_by_id(6)))

##TEST PACKAGE SEARCH PACKAGE BY OWNER

#c = Container()
#p1 = Container.Package('Apple', 3)
#p2 = Container.Package('Apple', 4)
#p3 = Container.Package('Cisco', 8)
#p4 = Container.Package('Cisco', 8)
#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#c.add_package(p4)
#print(c.show_packages_by_owner('Apple'))
#print(c.show_packages_by_owner('Cisco'))
#print(c.show_packages_by_owner('Dog'))

##TEST PACKAGE SEARCH PACKAGE BY WEIGHT

#c = Container()
#p1 = Container.Package('Apple', 3)
#p2 = Container.Package('Apple', 4)
#p3 = Container.Package('Cisco', 8)
#p4 = Container.Package('Cisco', 8)
#c.add_package(p1)
#c.add_package(p2)
#c.add_package(p3)
#c.add_package(p4)
#print(c.show_packages_by_weight(3))
#print(c.show_packages_by_weight(4))
#print(c.show_packages_by_weight(8))