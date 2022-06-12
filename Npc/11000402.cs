using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000402: Kiru
/// </summary>
public class _11000402 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001627$
    // - Uuugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001629$
                // - I need $item:20000060$ from $npcName:21000078$... to cleanse myself...
                return -1;
            case (30, 0):
                // $script:0831180407001630$
                // - This toxin... stronger than I thought... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
