using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001297: Tara
/// </summary>
public class _11001297 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005011$
    // - I can't stand this...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005641$
                // - If nobody stands up to injustice, then we all suffer.
                return 40;
            case (40, 1):
                // $script:1227194507005642$
                // - Just because others turn a blind eye, that doesn't mean that <i>we</i> should. If something is wrong, then we must work to make it right.
                return 40;
            case (40, 2):
                // $script:1227194507005643$
                // - Otherwise, it all becomes a vicious cycle. People like us need to act or nothing will ever change.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
