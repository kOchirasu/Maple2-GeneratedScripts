using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004218: Char
/// </summary>
public class _11004218 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010778$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010779$
                // - This world is ruled by competition. Only the best win.
                return 10;
            case (10, 1):
                // $script:0806222707010780$
                // - If you wanna survive, you've got to win, and there's no right or wrong when it comes to winning. Somebody's got to go, you or them.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
