package com.gfg.employeaap.repository;

import com.gfg.employeaap.entity.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepo extends JpaRepository<Employee, Integer> {

}
