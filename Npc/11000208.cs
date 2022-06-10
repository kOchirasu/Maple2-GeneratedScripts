using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000208: Nick
/// </summary>
public class _11000208 : NpcScript {
    internal _11000208(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000892$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407000894$ 
                // - There's been plenty of talk about Captain $npcName:11000044[gender:0]$'s leadership in Dark Wind, but I like his style. He said he'd evaluate every member based on their skill and performance. That's fair and reasonable. 
                // $script:0831180407000895$ 
                // - Those who have problems with it clearly just aren't good enough. 
                return true;
            case 30:
                // $script:0831180407000896$ 
                // - Follow this road southward to find the Barrota Trading Company's warehouse at the end. Start your search there, and you should find $item:20000046$. 
                return true;
            default:
                return true;
        }
    }
}
