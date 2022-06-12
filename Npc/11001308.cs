using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001308: Dunbard
/// </summary>
public class _11001308 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1215203907005027$
    // - Hello!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1227194507005653$
                // - Do you need something?
                return 30;
            case (30, 1):
                // $script:1227194507005654$
                // - If I don't have it, then it probably doesn't exist. I'm also interested in buying rare and unusual pieces.
                return 30;
            case (30, 2):
                // $script:1227194507005655$
                // - Take a look! I'm sure something will catch your fancy.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
