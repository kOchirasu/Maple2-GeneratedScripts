using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000981: Christopher
/// </summary>
public class _11000981 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180610001130$
    // - Ahoy! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001131$
                // - The Marco has a noble purpose, to transport adventurers on missions for the $map:02000068$. And lately, it's also been carrying adventurers to $map:02000183$ where they battle pirates in the eastern straits. If you're one of these adventurers, then you can board the ship for 4,000 mesos. Is that what you want to do?
                return -1;
            case (40, 0):
                // $script:0831180610001135$
                // - You need something?
                switch (selection) {
                    // $script:0831180610001136$
                    // - Can I board the ship?
                    case 0:
                        return 41;
                    // $script:0831180610001137$
                    // - I'm just looking around.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180610001138$
                // - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board.
                return -1;
            case (42, 0):
                // $script:0831180610001139$
                // - Taking a break from adventuring, eh? Nice. Wish I could do that, but this dock isn't going to manage itself.
                return -1;
            case (50, 0):
                // $script:0831180610001140$
                // - The operation of the Marco is mostly paid by the $map:02000068$, so the passengers only pay a small fare of 4,000 mesos. If you want to board, that's your price.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (1, 0) => NpcTalkButton.TakeBoat,
            _ => NpcTalkButton.None,
        };
    }
}
