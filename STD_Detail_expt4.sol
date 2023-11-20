pragma solidity ^0.6;
contract student_management{
    
    struct Student
    {
        int stud_id;
        string Name;
        string department;
    }

    Student[] std;

    function set_std_detail(int stud_id, string memory Name, string memory department) public {
	     Student memory stud = Student(stud_id,Name,department);
         std.push(stud);
    }

    function Get_detail(int stud_id) public view returns(string memory,string memory){
	    for(uint i=0;i<std.length;i++)
         {
            Student memory stud = std[i];
            if(stud.stud_id==stud_id)
            {
                return(stud.Name,stud.department);
            }  
        }
        return("Not Found","Not Found");
    }
}

