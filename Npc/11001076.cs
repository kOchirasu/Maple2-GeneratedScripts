using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001076: Slacky
/// </summary>
public class _11001076 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003671$
    // - Have you been to $map:02000051$?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003674$
                // - One day, I'm going to become as great a weaponsmith as my big brother!
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
