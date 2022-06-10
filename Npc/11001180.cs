using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001180: Mayar
/// </summary>
public class _11001180 : NpcScript {
    internal _11001180(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1110150406000967$ 
                // - Ooh... Everything here is so interesting!
                return true;
            case 30:
                // $script:1110150406000970$ 
                // - This place seems so peaceful. And everyone has such strange clothes! What's that person eating? I have so many questions!
                // $script:1110150406000971$ 
                // - ...Ah! Yalario! Are you from around here? It is nice to meet you.
                switch (selection) {
                    // $script:1110150406000972$
                    // - Yala-what-io?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1110150406000973$
                    // - You sure have a lot of questions.
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1110150406000974$
                    // - Where exactly are you from?
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1110150406000975$ 
                // - Hehe... Yalario is a greeting in my language. It means <b>awaited stranger</b>! Although, the literal translation is more like "well-groomed beard."
                return true;
            case 32:
                // $script:1110150406000976$ 
                // - How could I not? Visiting a new place is so exciting! I can't wait to learn more about this land and its people.
                // $script:1110150406000977$ 
                // - There are so many different types of people here! You must have lots of festivals and holidays of your own. I can't wait to see them!
                return true;
            case 33:
                // $script:1110150406000978$ 
                // - Mm... It is a distant land. You probably haven't heard of it. We traveled a great distance by ship to get here. Our village was not at all like this Town of Queens.
                return true;
            default:
                return true;
        }
    }
}
