public interface ProductRepository extends JpaRepository<Product, Long> {
  @EntityGraph(attributePaths = "category")
  List<Product> findByCategoryId(Byte categoryId);

  /// Custom query to reduce number of db requests and perform joins on data
  /// Does not conform to JpaRepository class, must add `@Query`
  @EntityGraph(attributePaths = "category")
  @Query("SEELCT p FROM Product p")
  List<product> findAllWithCategory();
}
