using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000503: Armano
/// </summary>
public class _11000503 : NpcScript {
    internal _11000503(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002184$ 
                // - What is it?
                return true;
            case 10:
                // $script:0831180407002185$ 
                // - Ah, $MyPCName$! Good to see you again. I made it home safely, all thanks to you. I thought Dad would be mad, but he let me in without saying a word. 
                // $script:0831180407002186$ 
                // - I've decided to stay out of trouble and be good. Come back and visit, will you?
                return true;
            default:
                return true;
        }
    }
}
