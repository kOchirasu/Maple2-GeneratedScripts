using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001514: Lolly
/// </summary>
public class _11001514 : NpcScript {
    internal _11001514(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0419105410001490$ 
                // - How may I help you look your best? 
                return true;
            case 1:
                // $script:0420153110001495$ functionID=1 
                // - Hiiii, $MyPCName$! I'm $npcName:11001513[gender:0]$'s assistant! He lets me handle the $itemPlural:20300246$! If you have some, I can give you an absolutely darling hairstyle! 
                switch (selection) {
                    // $script:0420153110001496$
                    // - Sure, let's spend some $itemPlural:20300246$.
                    case 0:
                        Id = 0;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
