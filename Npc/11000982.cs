using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000982: Christopher
/// </summary>
public class _11000982 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:0831180610001141$
    // - Ahoy! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610001142$
                // - $MyPCName$, what you did was fantastic!
                //   Now all you have to do is return to $map:02000062$ for a debriefing.
                //   It's 4,000 mesos to go back on the ship, the same fare as before.
                //   Do you want to depart for $map:02000062$ now?
                return -1;
            case (40, 0):
                // $script:0831180610001146$
                // - You need something?
                switch (selection) {
                    // $script:0831180610001147$
                    // - Can I board the ship?
                    case 0:
                        return 41;
                    // $script:0831180610001148$
                    // - I'm just looking around.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180610001149$
                // - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board.
                return -1;
            case (42, 0):
                // $script:0831180610001150$
                // - This place isn't too safe. You'd better be careful.
                return -1;
            case (50, 0):
                // $script:0831180610001151$
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
