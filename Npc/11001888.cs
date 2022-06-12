using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001888: Joanna
/// </summary>
public class _11001888 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1027193507007340$
    // - Good, very good!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1027193507007341$
                // - The filming went smoothly, thanks to you. Anyway, it's getting late, so I'm heading back to the station. I'll see you in $map:02000164$.
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
