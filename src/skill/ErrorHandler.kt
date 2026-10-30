package skill.core

class SkillException(val code: Int, val message: String, val details: String? = null) : RuntimeException(message)

object ErrorHandler {
    fun <T> handle(block: () -> T): T {
        try {
            return block()
        } catch (e: SkillException) {
            throw e
        } catch (e: IllegalArgumentException) {
            throw SkillException(400, "Invalid argument: ${e.message}", e.toString())
        } catch (e: Throwable) {
            throw SkillException(500, "Internal Skill error: ${e.message}", e.toString())
        }
    }
}
