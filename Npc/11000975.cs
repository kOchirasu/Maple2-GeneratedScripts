using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000975: Palmer
/// </summary>
public class _11000975 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003373$
    // - Unngh... Unngh... Unngh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003375$
                // - I believe if I work hard now, I'll be able to retire and spend time with my daughter someday.
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
