using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003254: Kaitlyn
/// </summary>
public class _11003254 : NpcScript {
    internal _11003254(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008175$ 
                // - What is it?
                return true;
            case 30:
                // $script:0403155707008176$ 
                // - I don't know what you did to impress $npcName:11003250[gender:0]$, but I'm not convinced. So, how are you going to prove that you're worth my time? 
                // $script:0403155707008177$ 
                // - <font color="#909090">($npc:11003254[gender:1]$'s voice drops to a whisper.)</font>
                //   <font size='20'>This is all for Professor $npc:11003148[gender:0]$...</font>
                return true;
            default:
                return true;
        }
    }
}
