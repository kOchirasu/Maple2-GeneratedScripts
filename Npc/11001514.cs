using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001514: Lolly
/// </summary>
public class _11001514 : NpcScript {
    protected override int First() {
        return 1;
    }

    // Select 0:
    // $script:0419105410001490$
    // - How may I help you look your best?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // functionID=1 
                // $script:0420153110001495$
                // - Hiiii, $MyPCName$! I'm $npcName:11001513[gender:0]$'s assistant! He lets me handle the $itemPlural:20300246$! If you have some, I can give you an absolutely darling hairstyle!
                switch (selection) {
                    // $script:0420153110001496$
                    // - Sure, let's spend some $itemPlural:20300246$.
                    case 0:
                        return 0;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (1, 0) => NpcTalkButton.SelectableBeauty,
            _ => NpcTalkButton.None,
        };
    }
}
