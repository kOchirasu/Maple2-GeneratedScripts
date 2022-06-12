using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001378: Boh
/// </summary>
public class _11001378 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005369$
    // - Ugh... Who's there?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005372$
                // - My head is spinning like a top... Or is it the world that's spinning? I feel like... I'm gonna die...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
