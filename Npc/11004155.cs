using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004155: Fufu
/// </summary>
public class _11004155 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010581$
    // - Ugh!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010582$
                // - Ugh! I'm all stiff from standing around all day. I can't wait to get off work.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
