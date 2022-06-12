using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000894: Aina
/// </summary>
public class _11000894 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003264$
    // - Everyone, wake up! We need to be alert.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003265$
                // - May the winds bring you comfort.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
