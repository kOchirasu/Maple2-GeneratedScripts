using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000200: Neal
/// </summary>
public class _11000200 : NpcScript {
    internal _11000200(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000869$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000872$ 
                // - $npcName:11000202[gender:0]$ is really dumb. Did you see him standing there? He's punishing himself!  
                return true;
            case 40:
                // $script:0831180407000873$ 
                // - $npcName:11000201[gender:0]$ is my friend from $map:02000023$. He's an elf. Isn't that awesome?  
                return true;
            default:
                return true;
        }
    }
}
