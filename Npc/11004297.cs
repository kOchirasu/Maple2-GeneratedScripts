using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004297: Ghost
/// </summary>
public class _11004297 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011375$
    // - I said I wanted the best. <i>The best!</i>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011378$
                // - I told my son to book me a room in the empire's finest hotel, and he put me up in <i>this</i> dump. Lo and behold, a picture frame dropped on my head while I slept, and now I'm dead! The other ghosts will laugh me out of town when they hear about this...
                switch (selection) {
                    // $script:1002141907011379$
                    // - There, there. It's okay.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011380$
                // - Just be careful around anything that hangs on a wall, okay? You never know when it'll fall!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
