using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001041: Makrasha
/// </summary>
public class _11001041 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003556$
    // - How did you find this place?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003559$
                // - When I close my eyes and listen carefully, I can hear everything... Everything in the entire world.
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
