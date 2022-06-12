using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000192: Ben
/// </summary>
public class _11000192 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407000864$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000866$
                // -  When I was young this place was a lush forest, but now it's nothing more than a sea of stumps and cabins.
                return 20;
            case (20, 1):
                // $script:0831180407000867$
                // - Thus, "$map:02000059$." Just look around and you'll see all the empty cabins that were once occupied by loggers.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
