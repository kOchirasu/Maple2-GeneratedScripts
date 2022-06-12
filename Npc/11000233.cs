using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000233: Brittany
/// </summary>
public class _11000233 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000987$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000989$
                // - Excuse me, what did you say?
                switch (selection) {
                    // $script:0831180407000990$
                    // - Have you seen $npcName:11000064[gender:0]$?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000991$
                // - I don't know. I don't think so. This place is small enough that newcomers should be easy to spot, and the last person who settled here was $npcName:11000006[gender:0]$.
                return -1;
            case (30, 0):
                // $script:0831180407000992$
                // - As you can see, $map:02000100$ suffers from a huge gap between the rich and the poor. It's all because of $npcName:11000065[gender:0]$ and $npcName:11000252[gender:0]$.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
