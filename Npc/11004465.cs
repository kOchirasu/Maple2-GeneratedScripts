using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004465: Richmonde Guard
/// </summary>
public class _11004465 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012093$
    // - Who goes there? Enemy?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012095$
                // - Who goes there? Enemy?!
                switch (selection) {
                    // $script:0111125107012684$
                    // - Hey, I'm on your side.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012096$
                // - Hm? Your clothes are strange, but you look like you can hold your own. You ever consider a career in freedom fighting?
                switch (selection) {
                    // $script:1227192907012097$
                    // - Sorry, but I've got other obligations.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012098$
                // - Tch... What a waste of talent. Well, if you change your mind, it's not like we can afford to be picky...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
