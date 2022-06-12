using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000212: David
/// </summary>
public class _11000212 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;40
    }

    // Select 0:
    // $script:0831180407000900$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000902$
                // - You look like you're still wet behind the ears. Stay out of trouble until you learn the ropes.
                return -1;
            case (40, 0):
                // $script:0831180407000903$
                // - When you get out of here, move ten cells southeast, and then ten more cells northeast. You'll arrive at a small iron gate. That gate leads to $map:02000156$, where the godfather of Blackstar, $npcName:11000251[gender:0]$, resides.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
