using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000054: Luke
/// </summary>
public class _11000054 : NpcScript {
    internal _11000054(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000232$ 
                // - What? 
                return true;
            case 30:
                // $script:0831180407000235$ 
                // - Bah! $npcName:11000062[gender:1]$ said she would go attend the court with her dad. Why isn't my gramps saying anything? I want to go to see the empress too! 
                return true;
            case 40:
                // $script:0831180407000236$ 
                // - $npcName:11000056[gender:0]$ knows about a lot of things. If you have questions, you should ask him! 
                return true;
            default:
                return true;
        }
    }
}
