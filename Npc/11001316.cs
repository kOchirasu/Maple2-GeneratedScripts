using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001316: Masharr
/// </summary>
public class _11001316 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005035$
    // - What brings you to this place?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005698$
                // - I cannot see you, but I know you by voice, scent, and soul.
                return 40;
            case (40, 1):
                // $script:1227194507005699$
                // - Your soul is pure. Maybe you can do it...
                return 40;
            case (40, 2):
                // $script:1227194507005700$
                // - May you be blessed with good vibes.
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
