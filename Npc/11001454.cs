using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001454: Lanpir
/// </summary>
public class _11001454 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1122123706000873$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1122123706000874$
                // - What is it?
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
