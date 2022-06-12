using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000399: Dr. Robson
/// </summary>
public class _11000399 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001616$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001618$
                // - The more I think about it, the angrier I get! How could they stop me from going on vacation, and one that I've had planned for months? Maybe I should just leave and let them deal with the water.
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
