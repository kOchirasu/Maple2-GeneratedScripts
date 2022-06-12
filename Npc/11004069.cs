using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004069: Cheez
/// </summary>
public class _11004069 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010143$
    // - It's breezy up here!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010144$
                // - It's breezy up here!
                return 10;
            case (10, 1):
                // $script:0619202207010145$
                // - Huh? What do <i>you</i> want?
                switch (selection) {
                    // $script:0619202207010146$
                    // - $npcName:11000367$'s owner is worried...
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0619202207010147$
                // - That's too bad. $npcName:11000367$ and I were meant for each other. It was fate.
                switch (selection) {
                    // $script:0619202207010148$
                    // - How'd you two meet, anyway?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0619202207010149$
                // - How is that any of your business? Let's just say that Skittle saved me from a really tough situation.
                return 32;
            case (32, 1):
                // $script:0619202207010150$
                // - You should just wish us happiness, okay?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
