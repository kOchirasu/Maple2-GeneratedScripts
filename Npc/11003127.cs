using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003127: Rowen
/// </summary>
public class _11003127 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0131174207007912$
    // - The Lumiknights are watching you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007946$
                // - I don't know how big the Lumiknights' organization is, but our numbers in Tria are just a fraction of the whole.
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
