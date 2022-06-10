using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000430: Antoine
/// </summary>
public class _11000430 : NpcScript {
    internal _11000430(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;41
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001791$ 
                // - I'm so glad I decided to come to the beach. 
                return true;
            case 30:
                // $script:0831180407001793$ 
                // - $map:02000111$ is such a beautiful place to be! Except for the turtles. They're awful. 
                return true;
            case 40:
                // $script:0831180407001794$ 
                // - Mm? 
                switch (selection) {
                    // $script:0831180407001795$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001796$ 
                // - Not interested. 
                return true;
            default:
                return true;
        }
    }
}
