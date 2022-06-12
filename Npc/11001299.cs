using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001299: Allon
/// </summary>
public class _11001299 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1215203907005013$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228222807005744$
                // - Remember what the empress told you!
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
